'''
Cole Leavitt
CSC110
Programming Project 1
This program implements functions to calculate the area of different geometric shapes.
'''

# Define a class to encapsulate shape area calculations
class ShapeCalculator:
    @staticmethod
    def rectangle_area(base, height):
        '''
        Calculate the area of a rectangle.
        Args:
            base (float): Length of the base of the rectangle.
            height (float): Height of the rectangle.
        Returns:
            float: Area of the rectangle.
        '''
        return base * height

    @staticmethod
    def triangle_area(a, b, c):
        '''
        Calculate the area of a triangle using Heron's formula.
        Args:
            a (float): Length of side a of the triangle.
            b (float): Length of side b of the triangle.
            c (float): Length of side c of the triangle.
        Returns:
            float: Area of the triangle.
        '''
        s = (a + b + c) / 2
        return (s * (s - a) * (s - b) * (s - c)) ** 0.5

    @staticmethod
    def trapezoid_area(base_1, base_2, height):
        '''
        Calculate the area of a trapezoid.
        Args:
            base_1 (float): Length of the first base of the trapezoid.
            base_2 (float): Length of the second base of the trapezoid.
            height (float): Height of the trapezoid.
        Returns:
            float: Area of the trapezoid.
        '''
        return 0.5 * (base_1 + base_2) * height

    @staticmethod
    def circle_area(radius):
        '''
        Calculate the area of a circle.
        Args:
            radius (float): Radius of the circle.
        Returns:
            float: Area of the circle.
        '''
        pi = 3.1415
        return round(pi * radius ** 2, 2)

# Test cases
shapes = [
    ShapeCalculator.rectangle_area(5, 10),
    ShapeCalculator.triangle_area(3, 4, 5),
    ShapeCalculator.trapezoid_area(3, 6, 4),
    ShapeCalculator.circle_area(2)
]

shape_names = ["Rectangle", "Triangle", "Trapezoid", "Circle"]

# Calculate and display the area of each shape
for i, area in enumerate(shapes):
    print(f"{shape_names[i]} Area:", area)
