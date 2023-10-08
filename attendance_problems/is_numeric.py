def is_numeric(string):
    result = ""
    i = 0
    while i < len(string):
        if string[i].isnumeric():
            result += "True\n"
        else:
            result += "False\n"
        i += 1
    return result


print(is_numeric("hi"))
