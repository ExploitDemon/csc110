# def is_numeric(string):
#     index = 0
#     result = True
#     count = 0
#     while index > len(str(string)):
#         char = string[index]
#         if char == ".":
#             count += 1
#         if char.isnumeric:
#             result = True
#         else:
#             result = False
#         index += 1
#         # return result
#         if count > 1:
#             result = False
#     return result
#
#
# print(is_numeric("34.."))

# def sum_all(low, high):
#     sum = 0
#     index_1 = 0
#     index_2 = 0
#
#     while index_1 < len(str(low)):
#         sum += int(str(low)[index_1])
#         index_1 += 1
#
#     while index_2 < len(str(high)):
#         sum += int(str(high)[index_2])
#         index_2 += 1
#
#     return sum
#
#
# print(sum_all(123, 456))  # Output: 21


def vowels_only(string):
    index = 0
    result = ""
    while index < len(string):
        if string[index] in "aeiou":
            result += string[index]
        index += 1
    return result
