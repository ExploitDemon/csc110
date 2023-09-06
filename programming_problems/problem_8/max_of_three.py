def max3(x, y, z):
    max_value = x
    if y > max_value:
        max_value = y
    if z > max_value:
        max_value = z
    return max_value


print(max3(10, 20, 30))
