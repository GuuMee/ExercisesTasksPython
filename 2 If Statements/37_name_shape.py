"""
Write a program that determines the name of a shape from its number of sides. Read
the number of sides from the user and then report the appropriate name as part of
a meaningful message. Your program should support shapes with anywhere from 3
up to (and including) 10 sides. If a number of sides outside of this range is entered
then your program should display an appropriate error message.

"""

number_sides = int(input("Enter the number of sides: "))

if number_sides == 3:
    print("This is a triangle")
elif number_sides == 4:
    print("This can be square or rectangle")
elif number_sides == 5:
    print("This is pentagon")
elif number_sides == 6:
    print("This is hexagon")
elif number_sides == 7:
    print("This is heptagon")
elif number_sides == 8:
    print("This is octagon")
elif number_sides == 9:
    print("This is nonagon")
elif number_sides == 10:
    print("This is decagon")
else:
    print("ERROR! The sides out of range! ")
