def has_duplicate(lst):
    return len(lst) != len(set(lst))


def main():
    print(has_duplicate([]))  # False
    print(has_duplicate([1, 2, 3, 1]))  # True
    print(has_duplicate([1, "a", "b", 4, 5]))  # False
    print(has_duplicate([1, "a", "a", 2, 3, 4]))  # True


if __name__ == '__main__':
    main()
