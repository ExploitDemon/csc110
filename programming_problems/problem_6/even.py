# def is_even():
#     number = int(input("What is your lucky number?"))
#     if number % 2 == 0:
#         return True
#     else:
#         return False
#
#
# result = is_even()
# print(result)


def is_even():
    while True:
        try:
            number = int(input("What is your lucky number?"))
            if number % 2 == 0:
                return True
            else:
                return False
        except:
            print("Not a int :/")


result = is_even()
print(result)
