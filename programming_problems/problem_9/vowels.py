def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    index = 0
    while index < len(s):
        if s[index] in vowels:
            count += 1
        index += 1
    return count


def main():
    print(count_vowels(""))  # 0
    print(count_vowels("aaa"))  # 3
    print(count_vowels("AEIOU"))  # 5
    print(count_vowels("cysts"))  # 0


if __name__ == '__main__':
    main()
