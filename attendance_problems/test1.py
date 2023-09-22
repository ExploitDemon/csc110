def calculator(x, y, operator):
    _x = int(x)
    _y = int(y)
    if operator == "+":
        return _x + _y
    elif operator == "-":
        return _x - _y
    elif operator == "/":
        return _x / _y
    elif operator == "*":
        return _x * _y
    else:
        return "Error"


print(calculator("3", "2", "+"))


def range_of_three(x, y, z):
    _x = int(x)
    _y = int(x)
    _z = int(x)
    _max = x
    _min = x
    if y > _max:
        _max = _y
    elif z > _max:
        _max = _z
    else:
        return "Error"

    if y < _min:
        _min = y
    elif z < _min:
        _min = z
    else:
        return "Error"

    return _max - _min


print(range_of_three(10, 20, 30))
