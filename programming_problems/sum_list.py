# # Rachel Whitaker
# def sum_all(numbers):
#     i = 0
#     result = 0
#     while len(numbers) > i:
#         result += numbers[i]
#         i += 1
#     return result


def max_of_list(numbers):
    index = 0
    if numbers is not None:
        largest = numbers[0]
        while len(numbers) > index:
            if numbers[index] > largest:
                largest = numbers[index]
            index += 1
        return largest
    else:
        return None



