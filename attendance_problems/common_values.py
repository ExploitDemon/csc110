# Rachel Whitaker
def common_values(set1, set2):
    for element in set1:
        if element in set2:
            return True
    return False
