def greetings(name):
    #  also check whetether the name is "James Bond"
    if "Bond" == name:
        return "Welcome on board 007"
    elif "James Bond" in name:
        return "Welcome on board 007"
    else:
        return f"Hello, {name}"


def main():
    user_name = input("Enter your name: \n")
    print(greetings(user_name))

if __name__ == '__main__':
    main()