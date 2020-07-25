"""
Write a program that begins by reading a temperature from the user in degrees
Celsius. Then your program should display the equivalent temperature in degrees
Fahrenheit and degrees Kelvin. The calculations needed to convert between different
units of temperature can be found on the internet.
"""

KELVIN = 273.15
FAHRENHEIT = 32

# Read the input from the user
celsius = float(input("Enter the degrees in Celsius: "))

# Convert celsius to kelvin and fahrenheit
in_kelvin = celsius + KELVIN
in_fahrenheit = (celsius * 9/5) + FAHRENHEIT

# Display degrees in kelvin and fahrenheit
print("Your degree in Kelvin will be %.2f and in Fahrenheit will be %.2f" % (in_kelvin, in_fahrenheit))
