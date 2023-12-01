# Rachel Whitaker
def remove_and_append(original_list, to_remove_list, to_append_list):
    for item in to_remove_list:
        while item in original_list:
            original_list.remove(item)
    original_list.extend(to_append_list)
    return original_list


if __name__ == "__main__":
    test_list = [1, 2, 3]
    remove_and_append(test_list, [2, 3, 4], [10, 11])
    assert test_list == [1, 10, 11]
    print(test_list)  # prints: [1, 10, 11]
