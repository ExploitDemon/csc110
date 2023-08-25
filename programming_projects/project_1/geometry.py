'''
Cole Leavitt
CSC110
Programming Project 1
This program implements functions to calculate the area of different geometric shapes.
'''

# Define the base class for shapes
class Shape:
    def area(self):
        pass

# Define the class for rectangles
class Rectangle(Shape):
    def __init__(self, base, height):
        '''
        Initializes a rectangle with given base and height.
        Args:
            base (float): Length of the base of the rectangle.
            height (float): Height of the rectangle.
        '''
        self.base = base
        self.height = height

    def area(self):
        '''
        Calculates the area of the rectangle.
        Returns:
            float: Area of the rectangle.
        '''
        return self.base * self.height

# Define the class for triangles
class Triangle(Shape):
    def __init__(self, a, b, c):
        '''
        Initializes a triangle with given side lengths.
        Args:
            a (float): Length of side a of the triangle.
            b (float): Length of side b of the triangle.
            c (float): Length of side c of the triangle.
        '''
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        '''
        Calculates the area of the triangle using Heron's formula.
        Returns:
            float: Area of the triangle.
        '''
        s = (self.a + self.b + self.c) / 2
        return (s * (s - self.a) * (s - self.b) * (s - self.c)) ** 0.5

# Define the class for trapezoids
class Trapezoid(Shape):
    def __init__(self, base_1, base_2, height):
        '''
        Initializes a trapezoid with given base lengths and height.
        Args:
            base_1 (float): Length of the first base of the trapezoid.
            base_2 (float): Length of the second base of the trapezoid.
            height (float): Height of the trapezoid.
        '''
        self.base_1 = base_1
        self.base_2 = base_2
        self.height = height

    def area(self):
        '''
        Calculates the area of the trapezoid.
        Returns:
            float: Area of the trapezoid.
        '''
        return 0.5 * (self.base_1 + self.base_2) * self.height

# Define the class for circles
class Circle(Shape):
    def __init__(self, radius):
        '''
        Initializes a circle with given radius.
        Args:
            radius (float): Radius of the circle.
        '''
        self.radius = radius
        self.pi = 3.1415

    def area(self):
        '''
        Calculates the area of the circle.
        Returns:
            float: Area of the circle.
        '''
        return self.pi * self.radius ** 2

# Create a list of shape instances
shapes = [
    Rectangle(5, 10),
    Triangle(3, 4, 5),
    Trapezoid(3, 6, 4),
    Circle(2)
]

# Calculate and display the area of each shape
for shape in shapes:
    shape_name = shape.__class__.__name__
    print(f"{shape_name} Area:", shape.area())