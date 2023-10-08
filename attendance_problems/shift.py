# Rachel is gone
def shift_right(lst):
    if len(lst) == 0:
        return lst

    last_index = len(lst) - 1
    i = last_index

    while i > 0:
        lst[i] = lst[i - 1]
        i -= 1

    lst[0] = None
    return lst


def main():
    assert shift_right(["a", "b", "c", "d"]) == [None, "a", "b", "c"]


if __name__ == '__main__':
    main()
