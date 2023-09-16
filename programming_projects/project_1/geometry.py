"""
Cole Leavitt
CSC110
Programming Project 1
This program implements functions to calculate the area of different geometric shapes.
"""


def rectangle_area(base, height):
    """
    This function calculates the area of a rectangle.
    Args:
        base: the length of the base of the rectangle.
        height: the height of the rectangle.
    Returns:
        The area of the rectangle.
    """
    return base * height


def triangle_area(a, b, c):
    """
    This function calculates the area of a triangle using Heron's formula.
    Args:
        a: the length of the first side of the triangle.
        b: the length of the second side of the triangle.
        c: the length of the third side of the triangle.
    Returns:
        The area of the triangle.
    """
    s = (a + b + c) / 2
    return (s * (s - a) * (s - b) * (s - c)) ** 0.5


def trapezoid_area(base_1, base_2, height):
    """
    This function calculates the area of a trapezoid.
    Args:
        base_1: the length of the top base of the trapezoid.
        base_2: the length of the bottom base of the trapezoid.
        height: the height of the trapezoid.
    Returns:
        The area of the trapezoid.
    """
    return 0.5 * (base_1 + base_2) * height


def circle_area(radius):
    """
    This function calculates the area of a circle.
    Args:
        radius: the radius of the circle.
    Returns:
        The area of the circle, rounded to two decimal places.
    """
    return round(3.1415 * radius ** 2, 2)


def main():
    print(rectangle_area(4, 4.5))  # 18.0
    print(triangle_area(3, 4, 5))  # 6.0
    print(trapezoid_area(11, 25, 5))  # 90.0
    print(trapezoid_area(4, 20, 10))  # 120.0
    print(circle_area(20))  # 1256.0
    print(circle_area(4))  # 50.26


if __name__ == '__main__':
    main()
