def min_of_three(x, y, z):
    if x <= y and x <= z:
        return x
    elif y <= x and y <= z:
        return y
    else:
        return z


print(min_of_three(0, 1, 3))
