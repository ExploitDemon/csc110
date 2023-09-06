def sphere_volume(radius):
    _volume_calc = (4 / 3 * 3.1415 * radius ** 3)
    return round(_volume_calc, 2)


def sphere_area(radius):
    _area_calc = 4 * 3.1415 * radius ** 2
    return round(_area_calc, 2)


print(sphere_area(3))

print(sphere_volume(2))
