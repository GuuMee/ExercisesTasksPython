'''
In the previous exercise you created a program that converts a letter grade into the
equivalent number of grade points. In this exercise you will create a program that
reverses the process and converts from a grade point value entered by the user to a
letter grade. Ensure that your program handles grade point values that fall between
letter grades. These should be rounded to the closest letter grade. Your program
should report A+ for a 4.0 (or greater) grade point average.

'''

A = 4.0
A_MINUS = 3.7
B_PLUS = 3.3
B = 3.0
B_MINUS = 2.7
C_PLUS = 2.3
C = 2.0
C_MINUS = 1.7
D_PLUS = 1.3
D = 1.0
F = 0
INVALID = -1

letter = float(input("Enter grade point: "))

if letter == A:
    gp = "A+ or A"
elif letter == A_MINUS:
    gp = "A-"
elif letter == B_PLUS:
    gp = "B++"
elif letter == B:
    gp = "B"
elif letter == B_MINUS:
    gp = "B--"
elif letter == C_PLUS:
    gp = "C++"
elif letter == C:
    gp = "C"
elif letter == C_MINUS:
    gp = "C--"
elif letter == D_PLUS:
    gp = "D++"
elif letter == D:
    gp = "D"
elif letter == F:
    gp = "F"

if gp == INVALID:
    print("That wesn't a valid number of grade points.")
else:
    print("Your point is", gp, "letter grade.")
