"""
Write a program that reads a magnitude from the user and displays the appropriate
descriptor as part of a meaningful message. For example, if the user enters 5.5 then
your program should indicate that a magnitude 5.5 earthquake is considered to be a
moderate earthquake.
"""

magnitude = float(input("Enter the magnitude (e.g. 5.5): "))
earthquake = ''

if magnitude < 2.0:
    earthquake = "Micro"
elif 2.0 <= magnitude < 3.0:
    earthquake = "Very minor"
elif 3.0 <= magnitude < 4.0:
    earthquake = "Minor"
elif 4.0 <= magnitude < 5.0:
    earthquake = "Light"
elif 5.0 <= magnitude < 6.0:
    earthquake = "Moderate"
elif 6.0 <= magnitude < 7.0:
    earthquake = "Strong"
elif 7.0 <= magnitude < 8.0:
    earthquake = "Major"
elif 8.0 <= magnitude < 10.0:
    earthquake = "Great"
elif magnitude >= 10.0:
    earthquake = "Meteoric"

print("A magnitude %.1f earthquake is considered to be a %s earthquake." % (magnitude, earthquake))