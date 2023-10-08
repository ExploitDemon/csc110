# def first_divisible(start, number):
#     index = 0
#     result = 0
#     while len(start) > index:
#         if start[index] % number == 0:
#             result = start[index] * number


# def first_divisible(start, number):
#     index = 0
#     while index < len(start):
#         if start[index] % number == 0:
#             result = start[index] * number
#             return result
#         index += 1
#     return None

def first_divisible(start, number):
    current = start
    while current % number != 0:
        current += 1
    return current


def double(number, limit):
    result = number
    while result <= limit:
        result *= 2
    return result


def remove_digits(string):
    result = ""
    for char in string:
        if not char.isdigit():
            result += char
    return result


def pass_or_fail(actual, expected):
    if actual == expected:
        print("Pass")
    else:
        print("Fail")
