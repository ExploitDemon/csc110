# def maximum(*values):
#     max_value = None
#     for value in values:
#         if max_value is None or value > max_value:
#             max_value = value
#     return max_value


def min_max(*values):
    # min_value = None
    # max_value = None
    min_value = max_value = values[0]
    for value in values:
        if min_value is None or value < min_value:
            min_value = value
        elif max_value is None or value > max_value:
            max_value = value
    return min_value, max_value


print(min_max(1, 2, 3, 4, 5))
