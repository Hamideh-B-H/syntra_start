import statistics

def ask_file_path():
    """Ask the user to enter the CSV file path until a valid one is provided. 
       If the user enters 'Stop', the program quits.
    """

    correct_path = "./Module 1-Hamideh/bord.csv"

    while True:
        file_path = input("Where is the CSV file located (type 'Stop' to quit)? ")

        if file_path.lower() == "stop":
            print("End! You asked to stop the program.")
            break

        elif file_path == correct_path:
            return correct_path

        else:
            print("File path is not valid! Please try again.")


## Global variable to store all CSV lines so it can be used in other menu items as well.
contents = []  


def read_file():
    """Read the CSV file into a list of lists, skipping the header."""
    global contents

    target_file = ask_file_path()

    with open(target_file) as my_file:
        my_file.readline()  # Skip the first line (header)
        contents = []

        for line in my_file:
            line = line.rstrip("\n")
            line = line.split(";")
            contents.append(line)

    return contents

def menu():
    """
Display a menu for the user to get different information about the CSV data.

The function first reads the CSV file, then presents a numbered menu
allowing the user to select options that provide various insights
and summaries from the CSV data.

"""
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

    if number == 1:
        print_number_of_lines()
    elif number == 2:
        print_contents()
    elif number == 3:
        print_unique_dates()
    elif number == 4:
        statistics_stats()
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
        save_file()
    else:
        print("Enter a correct number.")



def print_number_of_lines() -> None:
    """Print the total number of lines in the CSV contents."""
    global contents
    count_lines = len(contents)
    print(f"Number of lines: {count_lines}.")


def print_contents():
    """Print each line of CSV contents in a readable and formatted way."""
    global contents
    for i, line in enumerate(contents, start=1):
        try:
            line_text = (
                f"Line {i}, started on {line[1]}, sent on {line[2]}, "
                f"{line[3]}, {line[4]}, {line[5]}, {line[6]}"
            )
            print(line_text)
        except IndexError:
            print(f"Line {i} is incomplete or malformed.")


def print_unique_dates():
    """Print the number of unique dates found in the second column of the CSV."""
    global contents
    dates = set()
    for line in contents:
        date = line[1].split(" ")[0]  # Extract only the date part
        dates.add(date)
    print(f"There are {len(dates)} unique dates:")
    print(dates)



def statistics_stats():
    """Calculate and print the average, maximum, and minimum of numbers from column 4."""
    global contents
    numbers = []

    for line in contents:
        if len(line) < 4 or line[3] == "":
            continue
        try:
            num = float(line[3].replace(",", "."))
            numbers.append(num)
        except ValueError:
            continue

    if numbers:
        average = statistics.mean(numbers)
        highest_number = max(numbers)
        lowest_number = min(numbers)
        print(average, highest_number, lowest_number)
    else:
        print("No valid numbers found in column 4.")


def colors():
    """Count different colors and find the most frequent one."""
    global contents
    colors_number = {}
    colors = []

    for line in contents:
        if line[5].lower() == "":
            continue
        colors.append(line[5].lower())

    for color in colors:
        colors_number[color] = colors.count(color)

    for color, count in colors_number.items():
        print(f"{color.upper()}: {count}")

    max_count = 0
    max_color = ""
    for color, count in colors_number.items():
        if count > max_count:
            max_count = count
            max_color = color

    print(f"The color that appears the most: {max_color.upper()}")


def print_place_names():
    """Print unique place names from column 5 of the CSV."""
    global contents
    places = set()
    for line in contents:
        if line[4].lower() == "":
            continue
        place = line[4].lower()
        places.add(place)

    print(f"Here are {len(places)} unique places:")
    print(places)


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


def print_id_stats():
    """Print missing IDs from column 1 of the CSV."""
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
        
def print_q_word_stats():
    """Print statistics about words in column 7 starting with or containing 'Q'."""
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


def save_file():
    """Save filtered CSV data (IDs, numbers, colors, and Q-words) to a new file."""
    global contents
    info = []

    for line in contents:
        if len(line) > 0 and line[0].strip() != "":
            id_ = line[0].strip()
        else:
            id_ = ""

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
            info.append([id_, number, color, q_word])

    file_name = input("Enter a file name: ")
    with open(file_name + ".csv", "w") as file:
        for row in info:
            file.write(";".join(row) + "\n")



"""Start the program by displaying the menu."""
if __name__ == "__main__":
    menu()


