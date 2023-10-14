# # Rachel Whitaker
# def remove_vowels_list(characters):
#     vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
#     for vowel in vowels:
#         while vowel in characters:
#             characters.remove(vowel)
#     return characters
#
#
# def remove_vowels_string(string):
#     vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
#     new_string = ""
#     for char in string:
#         if char not in vowels:
#             new_string += char
#     return new_string
#
#
# def main():
#     assert remove_vowels_list(["b", "a", "n", "a", "n", "a"]) == ["b", "n", "n"]
#
#     assert remove_vowels_string("banana") == "bnnn"
#
#
# if __name__ == '__main__':
#     main()


def indices_of_vowels(string):
    """Return list of indices of vowels in the input string"""

    indices = []
    for i, char in enumerate(string):
        if char in "aeiouAEIOU":
            indices.append(i)

    return indices


def main():
    assert indices_of_vowels("hello") == [1, 4]
    assert indices_of_vowels("") == []
    assert indices_of_vowels("aeiou") == [0, 1, 2, 3, 4]


if __name__ == '__main__':
    main()
