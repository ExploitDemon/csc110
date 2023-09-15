# """
# Cole Leavitt
# CSC110
# Programming Project 1
# This program implements functions to calculate the area of different geometric shapes.
# GIT commit hash::: ada454c4b42e1f64133eac4a03de03a15eb1dfb0
# """
#
#
# # Define the base class for shapes
# class Shape:
#     def area(self):
#         pass
#
#
# # Function to calculate the area of a rectangle
# def rectangle_area(base, height):
#     return base * height
#
#
# # Function to calculate the area of a triangle using Heron's formula
# def triangle_area(a, b, c):
#     s = (a + b + c) / 2
#     return (s * (s - a) * (s - b) * (s - c)) ** 0.5
#
#
# # Function to calculate the area of a trapezoid
# def trapezoid_area(base_1, base_2, height):
#     return 0.5 * (base_1 + base_2) * height
#
#
# # Function to calculate the area of a circle
# def circle_area(radius):
#     pi = 3.1415
#     return round(pi * radius ** 2, 2)
#
#
# # Test cases
# shapes = [
#     rectangle_area(5, 10),
#     triangle_area(3, 4, 5),
#     trapezoid_area(3, 6, 4),
#     circle_area(2)
# ]
#
# shape_names = ["Rectangle", "Triangle", "Trapezoid", "Circle"]
#
# # Calculate and display the area of each shape
# for i, area in enumerate(shapes):
#     print(f"{shape_names[i]} Area:", area)

print(not 0)