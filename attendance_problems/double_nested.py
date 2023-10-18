def double_listed(two_d_list):
    for i in range(len(two_d_list)):
        for j in range(len(two_d_list[i])):
            two_d_list[i][j] *= 2
    return two_d_list


def main():
    print(double_listed([
        [1, 2, 3, 4],
        [1, 2, 3, 4]
    ]))


if __name__ == '__main__':
    main()
