def sales_tax(dictionary):
    new_dictionary = {}
    for key, value in dictionary.items():
        new_dictionary[key] = round(value * 0.056, 2)
    return new_dictionary
