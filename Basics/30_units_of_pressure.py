"""
In this exercise you will create a program that reads a pressure from the user in kilopascals.
Once the pressure has been read your program should report the equivalent
pressure in pounds per square inch, millimeters of mercury and atmospheres. Use
your research skills to determine the conversion factors between these units.
"""

SQUARE_INCH = 6.895
MILLIMETERS_OF_MERCURY = 7.501
ATMOSPHERE = 101

# Read the input pressure from the user
pressure = float(input("Enter the pressure in kilopascals: "))

# Convert pressure to other units
in_per_square_inch = pressure / SQUARE_INCH
in_millimeters_of_mercury = pressure * MILLIMETERS_OF_MERCURY
in_atmospheres = pressure / ATMOSPHERE

# Display the result
print("Pressure in pounds per square inch will be %.2f" % in_per_square_inch)
print("Pressure in millimeters of mercury will be %.2f" % in_millimeters_of_mercury)
print("Pressure in atmospheres will be %.2f" % in_atmospheres)
