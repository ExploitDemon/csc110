def longest_string(data):
    longest = None
    for dictionary in data:
        try:
            for key, value in dictionary.items():
                if longest is None or len(value) > len(longest):
                    longest = str(value)
        except Exception as e:
            print(f"An error occurred: {e}")
    return longest


def main():
    data = [{'a': 'horse', 'b': 'caterpillar'}, {'a': 'camp', 'c': 'joker'}]
    print(longest_string(data))  # Outputs: caterpillar

    data = [{1: 'abc', 5: 'onetwothree'}, {2: 'abcd'}, {7: 'one two three'}]
    print(longest_string(data))  # Outputs: one two three


if __name__ == '__main__':
    main()
