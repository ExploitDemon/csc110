def absolute(n):
    try:
        n_to_int = int(n)
        if n_to_int > 0:
            return n_to_int
        else:
            return n_to_int * (-1)
    except ValueError:
        print("invalid int")


print(absolute(4))
print(absolute(-4))
print(absolute(0))