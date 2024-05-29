# Create a function that returns both the area and circumference of a circle given its radius.
import math

def circle_stats(radius):
    area = math.pi * radius * radius
    circumference = 2 * math.pi * radius
    return area, circumference

radius = float(input("Enter the radius of the circle: "))

area, circumference = circle_stats(radius)

print("The area of the circle is: ", area)

print("The circumference of the circle is: ", circumference)