def read_csv(file_name):
    result = {}
    with open(file_name, encoding="UTF-8") as file:
        for line in file:
            values = line.strip().split(',')
            key = values[0]
            try:
                result[key] = [float(x) for x in values[1:]]
            except ValueError:
                result[key] = values[1:]
    return result


def main():
    print(read_csv("stipends.csv"))
    # {"Peter": [1000.0],
    #  "Joan": [50500.0],
    #  "Mary": [2400.0]}

    print(read_csv("population.csv"))
    # {"Country": ["United States", "Brazil", "Mexico", "Canada"],
    #  "Population (in mil)": [331.0, 212.56, 128.93, 37.74]}


if __name__ == '__main__':
    main()
