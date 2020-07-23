"""
A polygon is regular if its sides are all the same length and the angles between all of
the adjacent sides are equal. The area of a regular polygon can be computed using
the following formula, where s is the length of a side and n is the number of sides:
                area = (n*s^2)/4*tan(pi/n)
Write a program that reads s and n from the user and then displays the area of a
regular polygon constructed from these values.

"""
import math


def area_polygon():
    s = int(input("Enter the length of a side: "))
    n = int(input("Enter the number of sides: "))
    area = (n * s ** 2) / 4 * math.tan(math.pi / n)
    print("Area of the Regular Polygon will be %.2f" % area)

# Results:
# Enter the length of a side: 23
# Enter the number of sides: 8
# Area of the Regular Polygon will be 438.24
