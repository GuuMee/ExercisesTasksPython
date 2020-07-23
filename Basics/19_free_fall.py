"""
Create a program that determines how quickly an object is traveling when it hits the
ground. The user will enter the height from which the object is dropped in meters (m).
Because the object is dropped its initial speed is 0 m/s. Assume that the acceleration
due to gravity is 9.8 m/s2. You can use the formula vf =sqrt(vi^2 + 2ad) to compute the
final speed, vf , when the initial speed, vi , acceleration, a, and distance, d, are known.
"""

from math import sqrt


def free_fal():
    height = int(input("Enter the height object is dropped in meters: "))
    initial = 0
    acceleration = 9.8
    v_f = sqrt(initial ** 2 + 2 * acceleration * height)
    print("The final speed of the object is %.2f" % v_f)

# Results:
# Enter the height object is dropped in meters: 23
# The final speed of the object is 21.23


# Define a constant for acceleration to gravity in m/s**2
GRAVITY = 9.8

# Read the height from the object is dropped
d = float(input("Height from which the object is dropped (in meters): "))

# Compute the final velocity
vf = sqrt(2*GRAVITY * d)

# Display the result
print("It will hit the ground at %.2f m/s." % vf)

# The Vi^2 term has not been included in the calculation because Vi is 0.
