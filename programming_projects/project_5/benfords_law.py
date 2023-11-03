"""
Cole Leavitt
CSC110 Project 5
 This module contains functions to analyze
    the distribution of leading digits in a dataset, and check if it follows
    Benford's Law.
"""


def csv_to_list(file_name):
    """
    Reads a CSV file and converts the data into a list of strings.

    Args:
        file_name (str): The name of the CSV file.

    Returns:
        data (list): A list of strings representing the data in the CSV file.
    """
    with open(file_name, "r", encoding="UTF-8") as file:  # Open file with
        # UTF-8 encoding
        data = []
        for line in file:
            elements = line.replace("\n", "").split(",")  # replace new line
            # expression with nothing and also split at commas
            for element in elements:  # iterate over the elements since we split
                if element.isdigit() or (
                        element.replace(".", "",
                                        1).isdigit()):  # if the element
                    # is a digit
                    element = float(element)
                    if element >= 1:  # Skip numbers less than 1
                        # Check if the number is an integer
                        if element.is_integer():
                            data.append(str(int(element)))
                        else:
                            data.append(str(element))
        return data


def count_start_digits(list_of_numbers):
    """
    Counts the frequency of each leading digit (1-9) in the list of numbers.

    Args:
        list_of_numbers (list): A list of numbers.

    Returns:
        counts (dict): A dictionary where the keys are the digits (1-9) and the
            values are the counts of each digit.
    """
    counts = {}
    for i in range(1, 10):
        counts[i] = 0

    for number in list_of_numbers:
        if number[0] == "0":
            number = number.lstrip("0.")  # Remove leading zeros and decimal
            # point
        if number:  # Check if number is not an empty string
            first_digit = int(str(number)[0])
            counts[first_digit] += 1
    return counts


def digit_percentages(counts):
    """
    Calculates the percentage of each leading digit in the dataset.

    Args:
        counts (dict): A dictionary where the keys are the digits (1-9) and
            the values are the counts of each digit.

    Returns:
        percentages (dict): A dictionary where the keys are the digits (
          1-9) and the values are the percentages of each digit.
    """
    total = sum(counts.values())

    if total == 0:
        percentages = {}
        for digit in counts.keys():
            percentages[digit] = 0
    else:
        percentages = {}
        for digit, count in counts.items():
            percentage = round((count / total) * 100, 4)
            percentage = round(percentage, 2)
            percentages[digit] = percentage

    return percentages


def check_benfords_law(percentages):
    """
    Checks whether the calculated percentages follow Benford's Law within a
    certain tolerance.

    Args:
        percentages (dict): A dictionary where the keys are the digits (
            1-9) and the values are the percentages of each digit.

    Returns:
        bool: True if the data follows Benford's Law, False otherwise.
    """
    benfords_law = {1: 30, 2: 17, 3: 12, 4: 9, 5: 7, 6: 6, 7: 5, 8: 5, 9: 4}
    for digit, percentage in percentages.items():
        if not (benfords_law[digit] - 10 <= percentage <=
                benfords_law[digit] + 10):
            return False
    return True


def main():
    """
    Calls test cases.

    Returns:
        None.
    """
    # Change this line to read the "stocks.csv" file
    list_of_numbers = csv_to_list("populations.csv")
    counts = count_start_digits(list_of_numbers)
    percentages = digit_percentages(counts)
    print(check_benfords_law(percentages))
    print(percentages)
    print(csv_to_list("places.csv"))


if __name__ == "__main__":
    main()
