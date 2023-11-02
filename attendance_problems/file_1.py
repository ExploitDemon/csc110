with open("test.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        clean_line = line.strip()
        print(clean_line)
