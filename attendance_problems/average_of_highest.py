def average_of_highest(x, y, z):
    highest = max(x, y, z)
    if highest == x:
        return (x + max(y, z)) / 2
    elif highest == y:
        return (y + max(x, z)) / 2
    else:
        return (z + max(x, y)) / 2

# Test Cases
assert average_of_highest(1, 3, 4) == 3.5
assert average_of_highest(6, 4, 2) == 5.0
assert average_of_highest(4, 2, 1) == 3.0
