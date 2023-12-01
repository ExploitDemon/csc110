def remove_names(lst):
    vowels = "aeiou"
    for i in range(len(lst) - 1, -1, -1):
        if lst[i][-1].lower() in vowels:
            lst.pop(i)
    return lst


names = ["Beatrice", "Philip", "Anna", "Peter"]
print(remove_names(names))
