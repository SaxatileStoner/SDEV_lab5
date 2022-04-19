"""
* Lab 5 - SDEV 300
* @author Christopher Stoner

* This lab will deal with File I/O, Exceptions, and OOP.
* Allows user to load one of two CSV files,
  and then perform histogram analysis and plots for selected
  variables on the datasets.

* PopChange.csv represents the population change for
  specific dates for U.S. regions.
    * Pop Apr 1
    * Pop Jul 1
    * Change Pop

* Housing.csv represents Housing data over an extended period of
  time describing home age, number of bedrooms and other variables.
    * AGE
    * BEDRMS
    * BUILT
    * ROOMS
    * UTILITY

* Specific statistics should include:
    * Count
    * Mean
    * Standard Deviation
    * Min
    * Max
    * Histogram
"""


import csv
import numpy as np
from matplotlib import pyplot as plt


def file_selection():
    """Get user's selection for the file the user wishes to load.
    Can be an int value ranging 1, 2, or 3.

    Returns:
        int: This is the main menu option returned, either 1, 2, or 3
    """
    print("\nSelect the file you want to analyze: ")
    print("1. Population Data")
    print("2. Housing Data")
    print("3. Exit the Program\n")

    ACCEPTED_OPTIONS = [1, 2, 3]
    while True:
        try:
            usr_option = int(input("\n> "))
            for a_options in ACCEPTED_OPTIONS:
                if a_options == usr_option:
                    return usr_option
            print("Not a valid option!\n")
        except ValueError:
            print("The value entered is not an int!\n")


def pop_col_selection():
    """Get user's selection for the column to be rendered for PopChange.csv

    Returns:
        str: single string value from the accepted options
        that correlates to the column selection.
    """
    print("\nSelect the Column you want to analyze: ")
    print("a. Pop Apr 1")
    print("b. Pop Jul 1")
    print("c. Change Pop")
    print("d. Exit Column")

    ACCEPTED_OPTIONS = ['a', 'b', 'c', 'd']
    while True:
        try:
            usr_option = str(input("\n> "))
            for a_option in ACCEPTED_OPTIONS:
                if a_option == usr_option:
                    return usr_option
            print("Not a valid option!\n")
        except ValueError:
            print("The value entered cannot be converted to a string!\n")


def housing_col_selection():
    """Get user's selection for the column to be rendered for Housing.csv

    Returns:
        str: single string value from the accepted options
        that correlates to the column selection.
    """
    print("\nSelect the Column you want to analyze: ")
    print("a. AGE")
    print("b. BEDRMS")
    print("c. BUILT")
    print("d. ROOMS")
    print("e. UTILITY")
    print("f. Exit Column")

    ACCEPTED_OPTIONS = ['a', 'b', 'c', 'd', 'e', 'f']
    while True:
        try:
            usr_option = str(input("\n> "))
            for a_option in ACCEPTED_OPTIONS:
                if a_option == usr_option:
                    return usr_option
            print("Not a valid option!\n")
        except ValueError:
            print("The value entered cannot be converted to a string!\n")


def pop_process(column):
    """Openes up the PopChange.csv file,
    processes what column to calculate and render,
    performs calculations on the selected column,
    renders selected column in on a histogram.


    Args:
        column (str): Correlates to the selected column
        a -> Pop Apr 1
        b -> Pop Jul 1
        c -> Change Pop
    """

    fields = []
    rows = []

    # Open csv file and append attrubutes to local arrays
    with open('csv_data/PopChange.csv', 'r', encoding='UTF-8') as csv_file:

        csv_reader = csv.reader(csv_file)

        fields = next(csv_reader)

        for row in csv_reader:
            rows.append(row)

    if column == 'a':
        col_index = fields.index("Pop Apr 1")

    elif column == 'b':
        col_index = fields.index("Pop Jul 1")

    elif column == 'c':
        col_index = fields.index("Change Pop")

    else:
        print("Undexpected Error! Column param not as expected!")
        return

    # Append all values of the selected column to
    # it's own array for calulating: Count, Mean,
    # Standard Deviation, Min, Max, Histogram
    col_values = []
    for row in rows:
        col_values.append(float(row[col_index]))

    col_count = len(col_values)
    col_mean = np.mean(col_values)
    col_std = np.std(col_values)
    col_min = np.min(col_values)
    col_max = np.max(col_values)

    print(f"\n{'':-^32}\n")
    print(f"{fields[col_index]} Count = {col_count}\n" +
          f"{fields[col_index]} Mean = {col_mean}\n" +
          f"{fields[col_index]} Standard Deviation = {col_std}\n" +
          f"{fields[col_index]} Min = {col_min}\n" +
          f"{fields[col_index]} Max = {col_max}\n" +
          f"Printing Histogram of {fields[col_index]}...")

    plt.hist(col_values, bins=100, range=(
        col_mean-(col_std), col_mean+(col_std)), )
    plt.title(fields[col_index] +
              " Histogram")
    plt.show()
    print(f"\n{'':-^32}\n")


def housing_process(column):
    """Openes up the Housing.csv file,
    processes what column to calculate and render,
    performs calculations on the selected column,
    renders selected column in on a histogram.


    Args:
        column (str): Correlates to the selected column
        a -> AGE
        b -> BEDRMS
        c -> BUILT
        d -> ROOMS
        e -> UTILITY
    """

    fields = []
    rows = []

    with open('csv_data/Housing.csv', 'r', encoding='UTF-8') as csv_file:
        csv_reader = csv.reader(csv_file)

        fields = next(csv_reader)

        for row in csv_reader:
            rows.append(row)

    if column == 'a':
        col_index = fields.index("AGE")

    elif column == 'b':
        col_index = fields.index("BEDRMS")

    elif column == 'c':
        col_index = fields.index("BUILT")

    elif column == 'd':
        col_index = fields.index("ROOMS")

    elif column == 'e':
        col_index = fields.index("UTILITY")

    else:
        print("Undexpected Error! Column param not as expected!")
        return

    # Append all values of the selected column to
    # it's own array for calulating: Count, Mean,
    # Standard Deviation, Min, Max, Histogram
    col_values = []
    for row in rows:
        col_values.append(float(row[col_index]))

    col_count = len(col_values)
    col_mean = np.mean(col_values)
    col_std = np.std(col_values)
    col_min = np.min(col_values)
    col_max = np.max(col_values)

    print(f"\n{'':-^32}\n")
    print(f"{fields[col_index]} Count = {col_count}\n" +
          f"{fields[col_index]} Mean = {col_mean}\n" +
          f"{fields[col_index]} Standard Deviation = {col_std}\n" +
          f"{fields[col_index]} Min = {col_min}\n" +
          f"{fields[col_index]} Max = {col_max}\n" +
          f"Printing Histogram of {fields[col_index]}...")

    plt.hist(col_values, bins="auto", range=(col_min, col_max))
    plt.title(fields[col_index] +
              " Histogram")
    plt.show()
    print(f"\n{'':-^32}\n")


def __main__():
    """__main_ branch

    Returns:
        int: exit code, non-zero exits with crit errors
    """
    print(f'{" Welcome to the Python Data Analysis App ":*^64}')
    # continue_flag will tell when to exit the main loop with options 1 and 2
    continue_flag = True

    while continue_flag:
        usr_option = file_selection()

        if usr_option == 1:  # Using PopChange.csv data
            print("You have entered Population Data!\n-----")

            pop_col_option = pop_col_selection()
            if pop_col_option == 'a':  # Pop Apr 1 -> column
                print("You have selected: Pop Apr 1")
                pop_process(pop_col_option)

            elif pop_col_option == 'b':  # Pop Jul 1 -> column
                print("You have selected: Pop Jul 1")
                pop_process(pop_col_option)

            elif pop_col_option == 'c':  # Pop Change Pop -> column
                print("You have selected: Change Pop")
                pop_process(pop_col_option)

            elif pop_col_option == 'd':
                print("Exiting Column menu...")

            else:
                print("\nUnexpected Error! Closing Program...\n")
                return 1

        elif usr_option == 2:  # Using Housing.csv data
            print("You have entered Housing Data!\n-----")

            housing_col_option = housing_col_selection()
            if housing_col_option == 'a':  # AGE -> column
                print("you have selected: AGE")
                housing_process(housing_col_option)

            elif housing_col_option == 'b':  # BEDRMS -> column
                print("you have selected: BEDRMS")
                housing_process(housing_col_option)

            elif housing_col_option == 'c':  # BUILT -> column
                print("you have selected: BUILT")
                housing_process(housing_col_option)

            elif housing_col_option == 'd':  # ROOMS -> column
                print("you have selected: ROOMS")
                housing_process(housing_col_option)

            elif housing_col_option == 'e':  # UTILITY -> column
                print("you have selected: UTILITY")
                housing_process(housing_col_option)

            elif housing_col_option == 'f':
                print("Exiting Column menu...")

            else:
                print("\nUnexpected Error! Closing Program...\n")
                return 1

        elif usr_option == 3:
            return 0  # Completely exits main
        else:
            print("\nUnexpected Error! Closing Program...\n")
            return 1  # Exits with non-zero exit code


if __name__ == '__main__':
    EXIT_CODE = __main__()
    if EXIT_CODE == 0:
        print(f'{" Goodbye! ":*^64}')
    else:
        print(f'{" Encountered Crit Error! ":*^64}')
