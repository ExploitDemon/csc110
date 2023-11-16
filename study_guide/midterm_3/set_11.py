# 2d lists - mutate inner lists I

def remove_first_last(lst):
    for inner_list in lst:
        if len(inner_list) > 1:
            inner_list.pop(0)
            inner_list.pop(-1)
        elif len(inner_list) == 1:
            inner_list.pop(0)


# 2d lists - mutate inner lists II

def remove_equal(lst):
    for inner_list in lst:
        if len(inner_list) > 1 and inner_list[0] == inner_list[-1]:
            inner_list.pop(0)
            inner_list.pop(-1)


# 2d lists - mutate inner lists III

def remove_longest(lst):
    for sub_lst in lst:
        if len(sub_lst[0]) > len(sub_lst[-1]):
            sub_lst.pop(0)
        elif len(sub_lst[0]) < len(sub_lst[-1]):
            sub_lst.pop(-1)


# Select specific keys -- vowels

def keep_double_vowels(dictionary):
    vowels = "aeiouAEIOU"
    new_dict = {}

    for key, value in dictionary.items():
        double_vowel = False
        for i in range(len(key) - 1):
            if key[i] in vowels and key[i + 1] in vowels:
                double_vowel = True
                break

        if double_vowel:
            new_dict[key] = value

    return new_dict


# # Test case
# test_dictionary = {"Beatrice": 21, "Paul": 25, "Peter": 23}
# filtered_dict = keep_double_vowels(test_dictionary)
# print(filtered_dict)  # Output: {'Beatrice': 21, 'Paul': 25}


def keep_double_letters(dictionary):
    new_dict = {}

    for key, value in dictionary.items():
        double_letter = False
        lower_key = key.lower()  # convert key to lowercase
        for i in range(len(lower_key) - 1):
            if lower_key[i] == lower_key[i + 1]:
                double_letter = True
                break

        if double_letter:
            new_dict[key] = value

    return new_dict


# Test case
test_dictionary = {"Anna": 21, "Lenny": 25, "Aaron": 34, "Robb": 10, "Jack": 20}
filtered_dict = keep_double_letters(test_dictionary)
print(
    filtered_dict)  # Output: {'Anna': 21, 'Lenny': 25, 'Aaron': 34, 'Robb': 10}
