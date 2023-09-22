# my_str = "Clint Eastwood"
# var = my_str[11] + my_str[1] + my_str[13]
#
#
# my_str = "dusty"
# _var = my_str[2] + my_str[3] + my_str[1] + my_str[0] + my_str[4]
#
# print(var)
# print(_var)
def four_letter_anagram(string, a, b, c, d):
    return f"{string}"[a] + f"{string}"[b] + f"{string}"[c] + f"{string}"[d]


def main():
    print(four_letter_anagram("dogs", 0, 3, 2, 1))
    print(four_letter_anagram("loin", 0, 2, 1, 3))
    print(four_letter_anagram("lugs", 3, 2, 1, 0))
    print(four_letter_anagram("reap", 3, 1, 2, 0))


if __name__ == '__main__':
    main()
