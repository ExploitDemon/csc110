# def hypotenuse(a, b):
#     c = (a ** 2 + b ** 2) ** 0, 5
#     return round(c, 2)
#
#
# print(hypotenuse(10, 10))
def hypotenuse(a, b):
    c = ((a ** 2) + (b ** 2)) ** 0.5
    return round(c, 2)


print(hypotenuse(10, 10))