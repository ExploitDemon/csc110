def sum_all(numbers):
    total = 0
    i = 0
    while i < len(numbers):
        total += numbers[i]
        i += 1
    return total


def main():
    value = sum_all([])
    assert value == 0, f"expected return value was 0, but function returned {value}"

    value = sum_all([0, 0, 0, 0, 0])
    assert value == 0, f"expected return value was 0, but function returned {value}"

    value = sum_all([1, -1, 2, -2, 3, -3])
    assert value == 0, f"expected return value was 0, but function returned {value}"

    value = sum_all([1, 2, 3, 4, 5])
    assert value == 15, f"expected return value was 15, but function returned {value}"

    print("All tests passed.")


if __name__ == '__main__':
    main()
