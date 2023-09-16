def age_milestone(age):
    message = ""

    if age < 18:
        message = "You are too young"

    elif age >= 18:
        message = "You may apply to join for the military"

        if age >= 21:
            message = "You may drink"

        if age >= 35:
            message = "You may run for president"

    return message


print(age_milestone(18))
print(age_milestone(30))
print(age_milestone(0))
print(age_milestone(45))
