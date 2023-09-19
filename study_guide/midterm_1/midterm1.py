# Question 1
def slope(x1, y1, x2, y2):
    m = (y2 - y1) / (x2 - x1)
    return round(m, 2)


def main():
    slope_1 = slope(5, 5, 10, 10)
    print(slope_1)
    slope_2 = slope(1, 4, 3, 4)
    print(slope_2)
    slope_3 = slope(0, 0, -3, 4)
    print(slope_3)


main()


# Question 2
def calculate_year_born():
    age_string = input("What's your age? ")
    age = int(age_string)
    year_born = 2023 - age
    message = "You were born in " + str(year_born)
    return message


def main():
    result = calculate_year_born()
    print(result)


main()


# Question 3
def is_square(width, height):
    if width == height:
        return True
    else:
        return False


def main():
    width_string = input("Enter your shape width: ")
    height_string = input("Enter your shape height: ")
    width = float(width_string)
    height = float(height_string)
    if is_square(width, height) == True:
        print("Your shape is a square.")
    else:
        print("Your shape is a rectangle.")


main()


# Question 4
def range_of_three(x, y, z):
    max = x
    if y > max:
        max = y
    if z > max:
        max = z
    min = x
    if y < min:
        min = y
    if z < min:
        min = z
    return max - min


def main():
    print(range_of_three(3, 2, 8))
    print(range_of_three(10, 2, 8))
    print(range_of_three(10, 2, -8))


main()
