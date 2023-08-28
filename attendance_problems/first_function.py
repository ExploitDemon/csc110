# def add_one(number):
#     return number +1

# def area(_radius):
#     return float(_radius * 3.145 ** 2)
#
#
# radius = 2
#
#
# if area is not None:
#     print(area(radius))
# else:
#     print("you're dumb")


def volume(radius, height):
    volume_of_cylinder = (3.1415 * (radius ** 2) * height)
    return volume_of_cylinder


result = volume(3, 5)
print(result)
