# # Rachel Whitaker
# def low_high(x, y):
#     return min(x, y), max(x, y)
#

def sum_and_multiplication(dct):
    total_sum = 0
    total_multiplied = 1
    for value in dct.values():
        total_sum += int(value)
        total_multiplied *= int(value)

        return total_sum, total_multiplied
