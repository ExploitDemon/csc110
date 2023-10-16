import csv


def csv_to_list(file_name):
    numbers = []
    with open(file_name) as f:
        reader = csv.reader(f)
        for row in reader:
            for item in row:
                if item and (item.isdigit() or is_float(item)):
                    numbers.append(item)
    return numbers


def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


def count_start_digits(numbers):
    counts = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
    for num in numbers:
        if num[0].isdigit():  # Check if the first character is numeric
            digit = int(num[0])
            if digit != 0:
                counts[digit] += 1
    return counts


def digit_percentages(counts):
    total = sum(counts.values())
    percentages = {digit: round(count / total, 2) for digit, count in counts.items()}
    return percentages


def check_benfords_law(percentages):
    benfords_law_range = {
        1: (28.5, 33),
        2: (15.5, 18.7),
        3: (11.4, 13.2),
        4: (8.5, 9.9),
        5: (6.5, 7.7),
        6: (5.7, 6.6),
        7: (4.75, 5.5),
        8: (4.75, 5.5),
        9: (4.2, 4.6)
    }

    for digit, percent in percentages.items():
        if percent < benfords_law_range[digit][0] or percent > benfords_law_range[digit][1]:
            return False
    return True


if __name__ == '__main__':
    numbers = csv_to_list("stocks.csv")
    counts = count_start_digits(numbers)
    percentages = digit_percentages(counts)
    print(percentages)
    print(check_benfords_law(percentages))
