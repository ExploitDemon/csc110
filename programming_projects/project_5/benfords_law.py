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
    # Open the file with UTF-8 encoding
    with open(file_name, "r", encoding="UTF-8") as file:
        # Initialize an empty list to store the data
        data = []
        # Iterate over each line in the file
        for line in file:
            # Remove new line characters and split the line at commas
            elements = line.replace("\n", "").split(",")
            # Iterate over each element in the line
            for element in elements:
                # Check if the element is a digit
                if element.isdigit() or element.replace(".", "", 1).isdigit():
                    # Convert the element to a float
                    element = float(element)
                    # Skip numbers less than 1
                    if element >= 1:
                        # Check if the number is an integer
                        if element.is_integer():
                            # Convert the number to an integer and then to a
                            #   string, and add it to the list
                            data.append(str(int(element)))
                        else:
                            # Convert the number to a string and add it to
                            #   the list
                            data.append(str(element))
        # Return the list of data
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
    # Initialize a dictionary to store the counts of each digit
    counts = {}
    for i in range(1, 10):
        counts[i] = 0

    # Iterate over each number in the list
    for number in list_of_numbers:
        # If the number starts with a zero, remove leading zeros and decimal
        #   point
        if number[0] == "0":
            number = number.lstrip("0.")
            # Check if number is not an empty string
        if number:
            # Get the first digit of the number
            first_digit = int(str(number)[0])
            # Increment the count of the first digit
            counts[first_digit] += 1
    # Return the counts of each digit
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
    # Calculate the total count of all digits
    total = 0
    for value in counts.values():
        total += value

    # Initialize the percentages dictionary
    percentages = {}

    # If total count is zero, set all percentages to zero
    if total == 0:
        for digit in counts.keys():
            percentages[digit] = 0
    else:
        # Calculate the percentage for each digit
        for digit, count in counts.items():
            # Calculate the percentage and round it to 4 decimal places
            percentage = round((count / total) * 100, 4)
            # Round the percentage to 2 decimal places
            percentage = round(percentage, 2)
            # Store the percentage in the dictionary
            percentages[digit] = percentage
    # Return the percentages of the digits
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
    # Compare each calculated percentage with the expected percentage
    #   according to Benford's Law
    for digit, percentage in percentages.items():
        if not (benfords_law[digit] - 10 <= percentage
                <= benfords_law[digit] + 10):
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
