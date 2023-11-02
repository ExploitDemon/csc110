def sum_nums(lst, n):
    total = 0
    for sublist in lst:
        for num in sublist:
            if num < n:
                total += num
    return total


def main():
    print(sum_nums([[2, 12, 2], [12, 5, 100, 9]], 10))  # 18
    print(sum_nums([[2, 12, 2], [10, 5, 10, 9]], 10))  # 18
    print(sum_nums([[2, 12, 2], [10, 5, 10, 9]], 0))  # 0
    print(sum_nums([], 10))  # 0


if __name__ == '__main__':
    main()
