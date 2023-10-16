# Rachel Whitaker


_numbers = [[1, 2, 3, 4], [], [3, 4, 5, 6]]


def nested_max(numbers):
    _max = None
    for i in range(len(numbers)):
        if not numbers[i]:  # Check if the sublist is empty
            continue
        for j in range(len(numbers[i])):
            if _max is None or numbers[i][j] > _max:
                _max = numbers[i][j]
    return _max


if __name__ == '__main__':
    print(nested_max(_numbers))
