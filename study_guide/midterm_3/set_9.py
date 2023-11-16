# Read a file
def most_common_vehicle(filename):
    # Initialize an empty dictionary to store vehicle makes and number of owners
    vehicle_owners = {}

    # Open the file and read it line by line
    with open(filename, 'r') as file:
        for line in file:
            # Split the line into make and number of owners
            make, owners = line.strip().split(',')
            # Convert the number of owners to an integer
            owners = int(owners)
            # If the make is already in the dictionary, add the new number of
            # owners to the existing value
            if make in vehicle_owners:
                vehicle_owners[make] += owners
            # Otherwise, add the make to the dictionary with the number of
            # owners as its value
            else:
                vehicle_owners[make] = owners

    # Initialize variables to store the make with the most owners and the
    # highest number of owners
    most_common_make = None
    largest_owners = None

    # Iterate over the dictionary items
    for make, owners in vehicle_owners.items():
        # If this make has more owners than the current most common make,
        # update the most common make and the highest number of owners
        if largest_owners is None or owners > largest_owners:
            most_common_make = make
            largest_owners = owners

    # Return the make with the most owners
    return most_common_make


# Read and Write Files

def get_supply_count(filename):
    total = 0
    with open(filename, "r", encoding="UTF-8") as file:
        for line in file:
            line = line.strip().split(" ")
            total += int(line[1])

    with open('total.txt', 'w', encoding="UTF-8") as file:
        file.write(str(total))


# def main():
#     # run this line to create the input text file for the next function
#     supplies = open("supplies.txt", "w")
#     supplies.write("tv 0\n")
#     supplies.write("mouse 100\n")
#     supplies.write("monitor 0\n")
#     supplies.write("speakers 12\n")
#     supplies.write("iphone 5\n")
#     supplies.close()
#     no need to change this chunk, just run it to see if you pass
#     all tests listed here
#     get_supply_count("supplies.txt")
#     value = int(open("total.txt", "r").read().strip())
#     print(value)
#
#
# if __name__ == '__main__':
#     main()

# Read and write files II

def repeat_file(in_file_name, out_file_name, n):
    with open(in_file_name, 'r', encoding="UTF-8") as in_file:
        content = in_file.read()
    with open(out_file_name, 'w', encoding="UTF-8") as out_file:
        out_file.write(content * n)


# def main():
#     # # run this to create the input file for the test
#     # input_file = open("input.txt", "w")
#     # input_file.write("hello there\n")
#     # input_file.close()
#     # no need to change this chunk, just run it to see if you pass
#     # all tests listed here
#     repeat_file("input.txt", "output.txt", 2)
#     test_file = open("output.txt").read()
#     print(test_file)
#
#     repeat_file("input.txt", "output.txt", 0)
#     test_file = open("output.txt").read()
#     print(test_file)
#
#
# if __name__ == '__main__':
#     main()


