def validate_age(age):
    age = f"{age}"
    if age.isnumeric():
        return True
    else:
        return False


print(validate_age(14))