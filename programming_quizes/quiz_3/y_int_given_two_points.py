from slope import slope
from y_int import y_intercept


def y_intercept_2(x1, y1, x2, y2):
    m = slope(x1, y1, x2, y2)
    beta = y_intercept(m, x1, y1)
    return beta


print(y_intercept_2(10, 20, 30, 50))
