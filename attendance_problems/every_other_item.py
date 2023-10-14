# def every_other(_list):
#     new_list = []
#     index = 0
#     while index < len(_list):
#         new_list.append(_list[index])
#         index += 2
#     return new_list
#
#
# def main():
#     print(every_other([0, 1, 2, 3, 4, 5, 6, 7, 8]))
#
#
# if __name__ == '__main__':
#     main()
#
#

# def longest_string(lst):
#     max_len = -1
#     res = ""
#     i = 0
#     while i < len(lst):
#         if len(lst[i]) > max_len:
#             max_len = len(lst[i])
#             res = lst[i]
#         i += 1
#     return res
#
#
# def main():
#     print(longest_string(["a", "ab", "x", "abc", "c"]))
#
#
# if __name__ == '__main__':
#     main()


# def string_to_even_list(string):
#     index = 0
#     new_list = []
#     while index < len(string):
#         if string[index].isnumeric():
#             if int(string[index]) % 2 == 0:
#                 new_list.append(int(string[index]))
#         index += 1
#     return new_list


# def remove_vowels(strings):
#     vowels = "AEIOUaeiou"
#     new_list = []
#     index = 0
#     while index < len(strings):
#         second_index = 0
#         new_str = ""
#         while second_index < len(strings[index]):
#             if strings[index][second_index] not in vowels:
#                 new_str += strings[index][second_index]
#             second_index += 1
#         new_list.append(new_str)
#         index += 1
#     return new_list

def remove_vowels(lst):
    vowels = "aeiouAEIOU"
    index = 0
    while index < len(lst):
        second_index = 0
        new_str = ""
        while second_index < len(lst[index]):
            if lst[index][second_index] not in vowels:
                new_str += lst[index][second_index]
            second_index += 1
        lst[index] = new_str
        index += 1


