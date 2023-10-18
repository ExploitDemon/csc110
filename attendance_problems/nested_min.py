

_numbers = [[1, 2, 3, 4], [], [3, 4, 5, 6]]


def nested_min(numbers):
    _min = None
    for i in range(len(numbers)):
        if not numbers[i]:  # Check if the sublist is empty
            continue
        for j in range(len(numbers[i])):
            if _min is None or numbers[i][j] < _min:
                _min = numbers[i][j]
    return _min


if __name__ == '__main__':
    print(nested_min(_numbers))
