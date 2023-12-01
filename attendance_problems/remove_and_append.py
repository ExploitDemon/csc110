# Rachel Whitaker
def remove_and_append(original_list, to_remove_list, to_append_list):
    for item in to_remove_list:
        while item in original_list:
            original_list.remove(item)
    for item in to_append_list:
        original_list.append(item)
