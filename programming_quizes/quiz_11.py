# Remove items in a 2d lst I

def remove_odds(lst):
    for i in range(len(lst)):
        for j in range(len(lst[i]) - 1, -1, -1):
            if lst[i][j] % 2 != 0:
                lst[i].pop(j)


# Remove items from 2D lst II

def remove_negatives(lst):
    for i in range(len(lst)):
        for j in range(len(lst[i]) - 1, -1, -1):
            if lst[i][j] < 0:
                lst[i].pop(j)


# Remove items from 2D lst III

def remove_strings(lst):
    for i in range(len(lst)):
        for j in range(len(lst[i]) - 1, -1, -1):
            if lst[i][j][0].lower() == lst[i][j][-1].lower():
                lst[i].pop(j)


# Remove items from list IV

def remove_vowel_ending(lst):
    vowels = "aeiou"
    for i in range(len(lst)):
        for j in range(len(lst[i]) - 1, -1 - 1):
            if lst[i][j][-1].lower() in vowels:
                lst[i].pop(j)


def remove_records(dictionary):
    keys_to_remove = []
    for k in dictionary.keys():
        if k[0].lower() == k[-1].lower():
            keys_to_remove.append(k)
    for key in keys_to_remove:
        dictionary.pop(key)
    return dictionary
