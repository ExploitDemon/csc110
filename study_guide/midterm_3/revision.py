def get_list(dictionary):
    lst = []
    for key, value in dictionary.items():
        for count in range(value):
            lst.append(key)
        # i = 1
        # while value and i <= value:
        #     lst.append(key)
        #     i += 1

    return lst


def main():
    items = {'shovel': 1, 'board': 2, 'pipe': 3, 'torch': 1}
    assert get_list(items) == ['shovel', 'board', 'board', 'pipe', 'pipe',
                               'pipe', 'torch']
    print('tests passed')


if __name__ == '__main__':
    main()
