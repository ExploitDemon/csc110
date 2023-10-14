def write_csv(data_dict, file_name):
    with open(file_name, 'w') as file:
        for key, values in data_dict.items():
            line = key + ',' + ','.join(map(str, values)) + '\n'
            file.write(line)


def main():
    my_data = {"Peter": [1000], "Joan": [50500], "Mary": [2400]}
    write_csv(my_data, "stipends.csv")

    my_data = {"Country": ["United States", "Brazil", "Mexico", "Canada"],
               "Population (in mil)": [331.00, 212.56, 128.93, 37.74]}
    write_csv(my_data, "population.csv")

if __name__ == '__main__':
    main()