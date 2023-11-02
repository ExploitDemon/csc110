def get_elements(dictionary, n):
    result = []
    for key, value in dictionary.items():
        if key[0].isupper() or key[-1].isupper() or value >= n:
            result.append(value)
    return result


def main() -> object:
    data = {'Alpha': 10, 'bravo': 25, 'charliE': 15, 'dELTa': 2}
    print(get_elements(data, 12))  # [10, 25, 15]


if __name__ == '__main__':
    main()
