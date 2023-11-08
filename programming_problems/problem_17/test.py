def read_csv(file_name):
    new_dictionary = {}

    with open(file_name, "r", encoding="UTF-8") as file:
        for line in file:
            print(line)
            values = line.strip().split(",")
            print(values)
            key = values[0]
            print(key)

            float_val = []

            for x in values[1:]:
                # s04
                if x.replace('.', '', 1).isdigit():
                    float_val.append(float(x))
                else:
                    float_val.append(x)

            new_dictionary[key] = float_val

    return new_dictionary


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
