def swap(dictionary, set_data):
    for key in set_data:
        if key in dictionary:
            value = dictionary[key]
            del dictionary[key]
            dictionary[value] = key


def main():
    dict_data = {'a': 'b', 'c': 'd', 'e': 'f'}
    set_data = {'c', 'e'}
    swap(dict_data, set_data)
    print(dict_data)  # {'a': 'b', 'd': 'c', 'f': 'e'}

    dict_data = {23: 24, 110: 120, 50: 45, 70: 50, 57: 1}
    set_data = {23, 110, 57}
    swap(dict_data, set_data)
    print(dict_data)  # {50: 45, 70: 50, 24: 23, 120: 110, 1: 57}

    dict_data = {23: 24, 110: 120, 50: 45, 70: 50, 57: 1}
    set_data = {100}
    swap(dict_data, set_data)
    print(dict_data)  # {23:24, 110:120, 50:45, 70:50, 57:1}


if __name__ == '__main__':
    main()
