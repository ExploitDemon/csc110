# Hustafa
def factorial(number):
    index = 1
    value = 1
    while index <= number:
        value *= index
        index += 1
    return value


print(factorial(4))
