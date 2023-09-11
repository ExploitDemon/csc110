"""
Cole Leavitt
Giit Commit Hash: 034e241f582adbced08ea78a5ca4cef74848f773
CSC110
Assignment - 1
This program defines functions to calculate and analyze grades.
"""


def letter_grade(grade):
    '''
    This function returns the letter grade based on a numeric grade.

    Args:
        grade (float): The numeric grade.

    Returns:
        str: The letter grade (A, B, C, D, E, or X).
    '''
    if 90 <= grade <= 100:
        return "A"
    elif 80 <= grade < 90:
        return "B"
    elif 70 <= grade < 80:
        return "C"
    elif 60 <= grade < 70:
        return "D"
    elif 0 <= grade < 60:
        return "E"
    else:
        return "X"


def pass_or_fail(_letter_grade):
    '''
    This function determines if a letter grade represents a pass or fail.

    Args:
        _letter_grade (str): The letter grade.

    Returns:
        str: "Pass" if the grade is A, B, C, or D, "Fail" if the grade is E, "Error" if the input is not a single letter.
    '''
    if len(_letter_grade) != 1:
        return "Error"

    if _letter_grade in ["A", "B", "C", "D"]:
        return "Pass"
    elif _letter_grade == "E":
        return "Fail"
    else:
        return "Error"


def point_grade(score, total_points):
    """
    This function calculates the percentage grade based on the score and total points.

    Args:
        score (float): The score obtained.
        total_points (float): The total points available.

    Returns:
        float: The percentage grade rounded to two decimal places.
    """
    percentage = (score / total_points) * 100
    return round(percentage, 2)


def get_grade_results(score, total_points):
    """
    This function generates a formatted string with grade information.

    Args:
        score (float): The score obtained.
        total_points (float): The total points available.

    Returns:
        str: A string containing the grade result, e.g., "Your grade is 56.25 (D - Pass)".
    """
    point_grade_value = point_grade(score, total_points)
    letter_grade_value = letter_grade(point_grade_value)
    pass_fail_status = pass_or_fail(letter_grade_value)
    result = f"Your grade is {point_grade_value} ({letter_grade_value} - {pass_fail_status})"
    return result


def main():
    # Test letter_grade function
    print(letter_grade(90))  # A
    print(letter_grade(80))  # B
    print(letter_grade(70))  # C
    print(letter_grade(60))  # D
    print(letter_grade(59))  # E
    print(letter_grade(-59))  # X
    print(letter_grade(110))  # X

    # Test pass_or_fail function
    print(pass_or_fail("B"))  # Pass
    print(pass_or_fail("E"))  # Fail
    print(pass_or_fail("ABCD"))  # Error

    # Test point_grade function
    print(point_grade(0, 100))  # 0.0
    print(point_grade(100, 100))  # 100.0
    print(point_grade(45, 80))  # 56.25
    print(point_grade(37, 40))  # 92.5

    # Test get_grade_results function
    print(get_grade_results(0, 100))  # Your grade is 0.0 (E - Fail)
    print(get_grade_results(45, 80))  # Your grade is 56.25 (D - Pass)
    print(get_grade_results(37, 40))  # Your grade is 92.5 (A - Pass)


if __name__ == '__main__':
    main()
