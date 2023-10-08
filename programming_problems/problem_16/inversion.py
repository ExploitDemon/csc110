def invert_dictionary(d):
    inverted_dict = {}

    for key, value in d.items():
        if value not in inverted_dict:
            inverted_dict[value] = [key]
        else:
            inverted_dict[value].append(key)

    return inverted_dict


# Test cases
print(invert_dictionary({"a": 7, "b": 8}))  # {7: ["a"], 8: ["b"]}
print(invert_dictionary({"a": 2, "b": 2}))  # {2: ["a", "b"]}
print(invert_dictionary({}))  # {}
