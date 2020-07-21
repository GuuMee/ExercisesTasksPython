"""
Many people think about their height in feet and inches, even in some countries that
primarily use the metric system. Write a program that reads a number of feet from
the user, followed by a number of inches. Once these values are read, your program
should compute and display the equivalent number of centimeters.

"""


def units_height():
    one_f = 12
    one_i = 2.54
    one_f_sm = one_f * one_i
    feets = float(input("Enter your height in feet: "))
    inches = float(input("Enter your height in inches: "))
    feets_sm = one_f_sm * feets
    inches_sm = one_i * inches
    print("Your height from feet to sm: %.2f, from inches to sm: %.2f" % (feets_sm, inches_sm))

#Results:
# Enter your height in feet: 23.42
# Enter your height in inches: 23.42
# Your height from feet to sm: 713.84, from inches to sm: 59.49
