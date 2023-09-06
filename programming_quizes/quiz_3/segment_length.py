def segment_length(x1, y1, x2, y2):
    length = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

    return round(length, 2)