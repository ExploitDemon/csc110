def differences(set_1, set_2):
    diff_1 = set_1.difference(set_2)
    diff_2 = set_2.difference(set_1)
    return len(diff_1) + len(diff_2)


def main():
    print(differences({1, 2, 3}, {2, 3, 4, 5}))  # 3
    print(differences({'john', 'mark', 'paul'}, {'john', 'mark'}))  # 1


if __name__ == '__main__':
    main()
