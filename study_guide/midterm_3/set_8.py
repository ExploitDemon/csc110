# Create new list I

def get_evens(integers):
    new_lst = []
    for num in integers:
        if num % 2 == 0:
            new_lst.append(num)
    return new_lst


# Create new list II

def get_evens_nested(lst):
    new_lst = []
    for sub_lst in lst:
        for element in sub_lst:
            if element % 2 == 0:
                new_lst.append(element)

    return new_lst


# Mutate list I -- .pop()

def remove_evens(integers):
    for i in range(len(integers) - 1, -1, -1):
        if integers[i] % 2 == 0:
            integers.pop(i)
    return integers


# Mutate list II -- .pop()
def remove_over_ten(lst):
    for i in range(len(lst) - 1, -1, -1):
        if lst[i] > 10:
            lst.pop(i)
    return lst
    # i = 0
    # while i < len(lst):
    #     if lst[i] > 10:
    #         lst.pop(i)
    #     else:
    #         i += 1
    # return lst


# Mutate list items

def replace_items_over_ten(lst):
    for i in range(len(lst) - 1, -1, -1):
        if lst[i] > 10:
            lst[i] = "OVER"
    return lst


def main():
    test_list = [10, 13, 6, 1, 30]
    print(replace_items_over_ten(test_list))


if __name__ == '__main__':
    main()
