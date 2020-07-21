
from math import pi
# Volume of a cylinder


def volume_of_cylinder():
    r = float(input("Enter the radius of the cylinder: "))
    h = float(input("Enter the height of the cylinder: "))
    volume = pi*(r**2)*h
    print("The volume of the cylinder will be %.1f" % volume)


# volume_of_cylinder()
# Enter the radius of the cylinder: 12
# Enter the height of the cylinder: 50
# The volume of the cylinder will be 22619.5
