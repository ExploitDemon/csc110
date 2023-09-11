def letter_grade(grade):
    if grade >= 90:
        return "A"
    elif grade >= 80:
        return "B"
    elif grade >= 70:
        return "C"
    elif grade >= 60:
        return "D"
    elif grade >= 0:
        return "E"
    else:
        return "X"


def pass_or_fail(letter_grade):
    if len(letter_grade) != 1:
        return "Error"
    elif letter_grade in ["A", "B", "C", "D"]:
        return "Pass"
    else:
        return "Fail"


def point_grade(score, total_points):
    percentage = (score / total_points) * 100
    return round(percentage, 2)


def get_grade_results(score, total_points):
    point_grade_value = point_grade(score, total_points)
    letter_grade_value = letter_grade(point_grade_value)
    pass_fail_status = pass_or_fail(letter_grade_value)
    result = f"Your grade is {point_grade_value} ({letter_grade_value} - {pass_fail_status})"
    return result


def main():
    # test letter_grade function
    print(letter_grade(90))  # A
    print(letter_grade(80))  # B
    print(letter_grade(70))  # C
    print(letter_grade(60))  # D
    print(letter_grade(59))  # E
    print(letter_grade(-59))  # X
    print(letter_grade(110))  # X

    # test pass_or_fail function
    print(pass_or_fail("B"))  # Pass
    print(pass_or_fail("E"))  # Fail
    print(pass_or_fail("ABCD"))  # Error

    # test point_grade function
    print(point_grade(0, 100))  # 0.0
    print(point_grade(100, 100))  # 100.0
    print(point_grade(45, 80))  # 56.25
    print(point_grade(37, 40))  # 92.5

    # test get_grade_results function
    print(get_grade_results(0, 100))  # Your grade is 0.0 (E - Fail)
    print(get_grade_results(45, 80))  # Your grade is 56.25 (E - Fail)
    print(get_grade_results(37, 40))  # Your grade is 92.5 (A - Pass)


if __name__ == '__main__':
    main()
