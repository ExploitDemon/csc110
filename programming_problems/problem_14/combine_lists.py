def combine(list1, list2):
    for item in list2:
        list1.append(item)


def main():
    test_list = []
    combine(test_list, [])
    print(test_list)  # []

    test_list = [1, 2, 3]
    combine(test_list, [1, 1])
    print(test_list)  # [1, 2, 3, 1, 1]

    test_list = [1, 2, 3, 1, 5]
    combine(test_list, [])
    print(test_list)  # [1, 2, 3, 1, 5]


if __name__ == '__main__':
    main()