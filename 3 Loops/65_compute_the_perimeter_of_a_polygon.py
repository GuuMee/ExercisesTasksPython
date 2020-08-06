"""
Write a program that computes the perimeter of a polygon. Begin by reading the x
and y values for the first point on the perimeter of the polygon from the user. Then
continue reading pairs of x and y values until the user enters a blank line for the
x-coordinate. Each time you read an additional coordinate you should compute the
distance to the previous point and add it to the perimeter. When a blank line is entered
for the x-coordinate your program should add the distance from the last point back
to the first point to the perimeter. Then it should display the total perimeter. Sample
input and output is shown below, with user input shown in bold:

Enter the x part of the coordinate: 0
Enter the y part of the coordinate: 0
Enter the x part of the coordinate: (blank to quit): 1
Enter the y part of the coordinate: 0
Enter the x part of the coordinate: (blank to quit): 0
Enter the y part of the coordinate: 1
Enter the x part of the coordinate: (blank to quit):
The perimeter of that polygon is 3.414213562373095

"""

from math import sqrt

perimeter = 0
# Read the coordinates of the first point
first_x = float(input("Enter the x part of the coordinate:"))
first_y = float(input("Enter the y part of the coordinate: "))

# Provide initial values for prev_x and prev_y
prev_x = first_x
prev_y = first_y

# Read the remaining coordinates
line = input("Enter tje x part of the coordinate (blank to quit:)")
while line != "":

    # Convert the x part to a number and read the y part
    x = float(line)
    y = float(input("Enter the y part of the coordinate: "))

    # Compute the distance to the previous point and add it to the perimeter
    dist = sqrt((prev_x - x)**2 + (prev_y - y)**2)
    perimeter = perimeter + dist

    # Set up prev_x and prev_y for the next loop iteration
    prev_x = x
    prev_y = y

    # Read the x part of the next coordinate
    line = input("Enter the x part of the coordinate (blank to quit): ")

    # Compute the distance from the last point to the first point and add it to the perimeter
    dist = sqrt((first_x - x)**2 + (first_y - y)**2)
    perimeter = perimeter + dist

print("The perimiter of that polygon is", perimeter)
