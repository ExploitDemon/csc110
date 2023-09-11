def reverse_string(s):
    reversed_str = ''
    index = len(s) - 1
    while index >= 0:
        reversed_str += s[index]
        index -= 1
    return reversed_str


def remove_spaces(s):
    no_spaces_str = ''
    index = 0
    while index < len(s):
        if s[index] != ' ':
            no_spaces_str += s[index]
        index += 1
    return no_spaces_str


def is_palindrome(s):
    s = remove_spaces(s)
    reversed_str = reverse_string(s)
    return s == reversed_str


def main():
    print(reverse_string("aeiou"))  # uoiea
    print(remove_spaces("ae io ua"))  # aeioua

    print(is_palindrome("noon"))  # True
    print(is_palindrome("deified"))  # True
    print(is_palindrome("go deliver a dare vile dog"))  # True


if __name__ == '__main__':
    main()