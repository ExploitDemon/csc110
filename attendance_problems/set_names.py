# Rachel Whitaker
def count_names(file_name):
    with open(file_name, "r", encoding="UTF-8") as file:
        names = set(line.strip() for line in file if line.strip())
    return len(names)


# assert count_names("names.txt") == 11
