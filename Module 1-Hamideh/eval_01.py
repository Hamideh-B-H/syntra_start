# A/
# Asks the user where the CSV file is located.
# Keeps asking until the file can be read successfully, or until the user types ‘Stop’ to end the program.

def ask_file_path():
    correct_path = ".//bord.csv"  # This is the expected correct file path
    while True:
        file_path = input("where is the CSV file located (Type Stop to stop asking)?")
        if file_path.lower() == "stop":  # Check if the user wants to quit
            print("End!You asked to stop the program!")
            break
        elif file_path == correct_path:  # Check if the path matches the correct path
            # print ("File is found!")
            return correct_path  # Return the correct path to use for reading
        else:
            print("file path is not valid! enter again!")  # Ask again if the path is wrong

# B/
# Reads the entire file. Ignore the first line (column names).
# The data structure in memory should be a list of lists, with the variable name contents.

contents = []  # Global variable to store all lines from the CSV for other functions to use

def read_file():
    global contents
    target_file = ask_file_path()  # Ask the user for the file path
    with open(target_file) as my_file:  # Open the file
        my_file.readline()  # Skip the first line (header)
        contents = []
        for line in my_file:  # Read each line
            line = line[:-1]  # Remove newline at the end
            line = line.split(";")  # Split line into a list using semicolon
            contents.append(line)  # Add line to contents
        # for line in contents:
        #     print(line)
        return contents  # Return the full contents

# Menu to allow user to select what to do with the CSV data
def menu():
    read_file()  
    print("You can select one of the following numbers to understand the file:")
    print("1: number of lines!")
    print("2: content line!")
    print("3: dates!")
    print("4: statistics!")
    print("5: color statistics!")
    print("6: place names!") 
    print("7: participation statistics!")
    print("8: ID statistics!")
    print("9: Q-word statistics!")
    print("10: Save a file!")

    number = int(input("Enter your number: "))

    # Calls the appropriate function based on user input.
    if number == 1:
        print_number_of_lines()
    elif number == 2:
        print_contents()
    elif number == 3:
        print_unique_dates()
    elif number == 4:
        statistics()
    elif number == 5:
        colors()
    elif number == 6:
        print_place_names()  
    elif number == 7:
        participation_stats() 
    elif number == 8:
        print_id_stats()
    elif number == 9:
        print_q_word_stats() 
    elif number == 10:
        save__file()
    else:
        print("Enter a correct number.")  # Inform user if input is invalid

# Prints total number of lines.
def print_number_of_lines () -> None:
    """Print the total number of lines in the contents."""
    global contents
    count_lines = len(contents)  # Count number of lines
    print(f"Number of lines: {count_lines}.")

# Prints each line in a readable way
def print_contents():
    """Print each line of contents in a readable and formatted way."""
    global contents
    for index, line in enumerate(contents, start=1):
        try:
            # Combine elements of line into a readable string
            line_text = (
                f"Line {index}, started on {line[1]}, sent on {line[2]}, "
                f"{line[3]}, {line[4]}, {line[5]}, {line[6]}"
            )
            print(line_text)
        except IndexError:  # Handle lines that are too short
            print(f"Line {index} is incomplete or malformed.")

# Shows unique dates from the second column.
def print_unique_dates():
    global contents
    dates = set()  # Use a set to store unique dates
    for line in contents:
        date_time = line[1].split(" ")  # Split date and time
        date = date_time[0]  # Take only the date part
        dates.add(date)
    print(f"There are {len(dates)} unique dates:")
    print(dates)

# Shows statistics (average, max, min) of numbers from column 4
def statistics():
    global contents
    random_numbers = []
    for line in contents:
        if len(line) < 4 or line[3] == "":
            continue  # Skip empty or missing numbers
        try:
            num = float(line[3].replace(",", "."))  # Convert to float
            random_numbers.append(num)
        except ValueError:  # Skip if conversion fails
            continue
    # Calculates average, max, min.
    average = sum(random_numbers)/len(random_numbers)
    highest_number = max(random_numbers)
    lowest_number = min(random_numbers)
    print(average, highest_number, lowest_number)

# Counts different colors and find the most frequent one.
def colors():
    global contents
    colors_number = {}
    colors = []

    for line in contents:
        if line[5].lower() == "":
            continue
        else:
            colors.append(line[5].lower())  

    for color in colors:
        colors_number[color] = colors.count(color)  

    for color, count in colors_number.items():
        print(f"{color.upper()}: {count}")
    
    # Finds the most frequents color.
    max_count = 0
    max_color = ""
    for color, count in colors_number.items():
        if count > max_count:
            max_count = count
            max_color = color

    print(f"The color that appears the most: {max_color.upper()}")

# Shows unique places (remove repeated ones) from column 5.
def print_place_names():
    global contents
    places = set()
    for line in contents:
        if line[4].lower() == "":
            continue
        else:
            place = line[4].lower()
            places.add(place)
    print(f"Here are {len(places)} unique places:")
    print(places)

# Shows number of complete and incomplete submissions.
def participation_stats():
    """Print the number of complete and incomplete submissions."""
    global contents
    complete = 0
    incomplete = 0

    for line in contents:
        if line[2].strip() != "":
            complete += 1
        else:
            incomplete += 1

    total = complete + incomplete
    print(f"There are {total} submissions: {complete} complete and {incomplete} incomplete.")

# Shows missing IDs in column 1
def print_id_stats():
    global contents
    ID_list = []
    missing_ID = []

    for line in contents:
        ID_list.append(int(line[0]))

    ID_list.sort()  

    for i in range(ID_list[0], ID_list[-1] + 1):
        if i not in ID_list:
            missing_ID.append(i)

    print(f"These values are missing: {missing_ID}")
        
# Shows statistics about words starting or containing Q in column 7
def print_q_word_stats():
    global contents
    q_words = []
    count_start_q = 0
    count_contain_q = 0
    count_no_q = 0 
    
    for line in contents:
        if len(line) > 6 and line[6].strip() != "":
            q_words.append(line[6].strip())
   
    for item in q_words:
        word = item.lower()  
        if word.startswith("q"):
            count_start_q += 1
        elif "q" in word:
            count_contain_q += 1
        else:
            count_no_q += 1

    print(f"{count_start_q} words start with Q")
    print(f"{count_contain_q} words contain a Q but not as the first letter")
    print(f"{count_no_q} contain no Q")

# Saves filtered data to a new CSV file
def save__file():
    global contents
    info = []

    for line in contents:
        if len(line) > 0 and line[0].strip() != "":
            id = line[0].strip()
        else:
            id = ""

        if len(line) > 3 and line[3].strip() != "":
            number = line[3].strip()
        else:
            number = ""

        if len(line) > 5 and line[5].strip() != "":
            color = line[5].strip()
        else:
            color = ""

        if len(line) > 6 and line[6].strip() != "" and line[6].strip().lower().startswith("q"):
            q_word = line[6].strip()
            info.append([id, number, color, q_word])
    
    file_name = input("Enter a file name: ")
    with open(file_name + ".csv", "w") as file:
        for row in info:
            file.write(";".join(row) + "\n")   

# calling the program by menu function.
menu()



