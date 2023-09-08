def greeting(first_name, last_name):
    return f"Hello, {first_name} {last_name}!"


def count_characters(name):
    length = len(name)
    return length


def main():
    _first_name = input("what is your first name? ")
    _last_name = input("What is your last name? ")

    greeting(_first_name, _last_name)
    # _len_of_first_name = int(count_characters(_first_name))
    # _len_of_last_name = int(count_characters(_last_name))
    _total_len = ((int(count_characters(_first_name))) + (int(count_characters(_last_name))))
    print(f"Your full name has {_total_len} letters.")


if __name__ == '__main__':
    main()
