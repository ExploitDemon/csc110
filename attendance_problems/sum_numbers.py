# Rachel Whitaker
def sum_all(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
        numbers = [int(line.strip()) for line in lines]
        total = sum(numbers)
    return total
