# def validate_age(age):
#     try:
#         age = int(age)
#         if 0 <= age <= 110:
#             return True
#         else:
#             return False
#     except ValueError:
#         return False


def check_eligibility(age):
    try:
        age = int(age)
        if age >= 18:
            return True
        else:
            return False
    except ValueError:
        return False


def validate_age(age):
    if age.isdigit():  # Check if the string consists of only digits
        age_as_int = int(age)
        if 0 <= age_as_int <= 110:
            return True
    else:
        return False


# def validate_age(age):
#     if age.isdigit():  # Check if the string consists of only digits
#         age_as_int = int(age)
#         if 0 <= age_as_int <= 110:
#             return True
#         else:
#             return False
#     else:
#         return False


def check_eligibility(age):
    return age >= 18


# Test cases
print(validate_age("20"))  # True
print(validate_age("20.5"))  # False
print(validate_age("20a"))  # False
print(validate_age("300"))  # False
print(check_eligibility(20))  # True
print(check_eligibility(15))  # False
