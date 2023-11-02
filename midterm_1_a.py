# def string_to_even_list(string):
#    list  = []
#    for char in string:
#        if char.isnumeric():
#            if int(char) % 2 == 0 :
#                list.append(char)
#    return list


def remove_odds(numbers):
    for number in range(len(numbers)):
        if number % 2 == 0:
            numbers.remove(number)


def main():
    #    print(string_to_even_list("12343asfasrfd"))
    print(remove_odds([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))


main()
