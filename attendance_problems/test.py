def calculate_year_born():
    try:
        age = int(input("Enter your age?: "))
        year_born = (2023 - age)
        return year_born
    except IndexError:
        print("invalid input")
