# Rachel Whitaker
def count_names(file):
    tracker = {}

    with open(file, 'r', encoding="UTF-8") as f:
        for line in f:
            if line.strip() != "":  # check if the line is not empty
                if line in tracker:
                    tracker[line] += 1
                else:
                    tracker[line] = 1

    return len(tracker.keys())
