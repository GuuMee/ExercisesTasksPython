from math import pi
"""
Write a program that begins by reading a radius, r, from the user. The program will
continue by computing and displaying the area of a circle with radius r and the
volume of a sphere with radius r. Use the pi constant in the math module in your
calculations.
"""


def area_and_volume():
    r = float(input("Enter the radius: "))
    area = pi * (r**2)
    volume = 4/3*pi*(r**3)
    print("The area of a circle: %.2f" % area)
    print("The volume of a sphere: %.2f" % volume)


# Enter the radius: 23
# The area of a circle: 1661.90
# The volume of a sphere: 50965.01
