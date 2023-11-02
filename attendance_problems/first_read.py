# Rachel Whitaker
def read_first_line(filename):
    with open(filename, 'r') as f:
        first_line = f.readline().rstrip()
    return first_line
