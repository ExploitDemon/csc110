"""
Cole Leavitt
CSC110 - Programming Project 3
This program implements functions to calculate mean, variance, standard deviation, and range of a list of numbers.
''"""


def mean(numbers):
    """Calculate the mean of a list of numbers.

    Args:
        numbers (list): A list of numbers.

    Returns:
        float: The mean of the numbers.
    """
    if not numbers:
        return 0
    total = 0
    count = 0
    while count < len(numbers):
        total += numbers[count]
        count += 1
    return round(total / len(numbers), 2)


def variance(numbers):
    """Calculate the variance of a list of numbers.

    Args:
        numbers (list): A list of numbers.

    Returns:
        float: The variance of the numbers.
    """
    if not numbers:
        return 0
    mean_value = mean(numbers)
    total = 0
    count = 0
    while count < len(numbers):
        total += (numbers[count] - mean_value) ** 2
        count += 1
    return round(total / (len(numbers) - 1), 2)


def sd(numbers):
    """Calculate the standard deviation of a list of numbers.

    Args:
        numbers (list): A list of numbers.

    Returns:
        float: The standard deviation of the numbers.
    """
    if not numbers:
        return 0
    variance_value = variance(numbers)
    sd_value = variance_value ** 0.5
    return round(sd_value, 2)


def list_range(numbers):
    """Calculate the range of a list of numbers.

    Args:
        numbers (list): A list of numbers.

    Returns:
        float: The range of the numbers.
    """
    if not numbers:
        return 0
    min_value = numbers[0]
    max_value = numbers[0]
    count = 1
    while count < len(numbers):
        if numbers[count] < min_value:
            min_value = numbers[count]
        if numbers[count] > max_value:
            max_value = numbers[count]
        count += 1
    return max_value - min_value


# Test cases
def main():
    """Test the functions in this module."""
    value = mean([])
    assert value == 0, \
        f"expected return value was 0, but function returned {value}"

    value = mean([0, 0, 0])
    assert value == 0, \
        f"expected return value was 0, but function returned {value}"

    value = mean([4, 5, 2])
    assert value == 3.67, \
        f"expected return value was 3.67, but function returned {value}"

    value = variance([4, 5, 2])
    assert value == 2.33, \
        f"expected return value was 2.33, but function returned {value}"

    value = sd([4, 5, 2])
    assert value == 1.53, \
        f"expected return value was 1.53, but function returned {value}"

    value = list_range([4, 5, 2])
    assert value == 3, \
        f"expected return value was 3, but function returned {value}"

    value = list_range([])
    assert value == 0, \
        f"expected return value was 0, but function returned {value}"

    print("All tests passed.")


if __name__ == '__main__':
    main()
