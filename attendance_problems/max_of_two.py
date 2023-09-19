# TA: Rachel

def max_of_two(one, two):
    max_value = one
    if two > max_value:
        max_value = two
    return max_value


print(max_of_two(-1, 3))
print(max_of_two(-1, -3))
print(max_of_two(5, 5))
