"""
In the previous exercise you created a program that computed the area of a triangle
when the length of its base and its height were known. It is also possible to compute
the area of a triangle when the lengths of all three sides are known. Let s1, s2 and s3
be the lengths of the sides. Let s = (s1 + s2 + s3)/2. Then the area of the triangle
can be calculated using the following formula:
area = sqrt(s × (s − s1) × (s − s2) × (s − s3))
Develop a program that reads the lengths of the sides of a triangle from the user and
displays its area.

"""

from math import sqrt


def triangle_area():
    s1 = float(input("Enter the 1st side length of a triangle: "))
    s2 = float(input("Enter the 2nd side length of a triangle: "))
    s3 = float(input("Enter the 3rd side length of a triangle: "))
    s = (s1 + s2 + s3) / 2
    area = sqrt(s * (s - s1) * (s - s2) * (s - s3))
    print("The area of the triangle by its 3 side will be %.2f" % area)


# Results:
# Enter the 1st side length of a triangle: 23
# Enter the 2nd side length of a triangle: 12
# Enter the 3rd side length of a triangle: 12
# The area of the triangle by its 3 side will be 39.42
