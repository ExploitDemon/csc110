def calculate_year_born():
    while True:
        try:
            age = int(input("Enter your age?: "))
            year_born = (2023 - age)
            print(f"You were born in {year_born}")
            return year_born
        except ValueError:
            print("invalid input")


calculate_year_born()