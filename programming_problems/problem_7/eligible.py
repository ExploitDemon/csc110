def validate_age(age):
    try:
        age = int(age)
        if 0 <= age <= 110:
            return True
        else:
            return False
    except ValueError:
        return False



def check_eligibility(age):
    try:
        age = int(age)
        if age >= 18:
            return True
        else:
            return False
    except ValueError:
        return False

