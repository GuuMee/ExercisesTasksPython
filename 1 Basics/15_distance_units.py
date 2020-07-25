"""
In this exercise, you will create a program that begins by reading a measurement
in feet from the user. Then your program should display the equivalent distance in
inches, yards and miles. Use the Internet to look up the necessary conversion factors
if you don’t have them memorized.

"""


def change_feet_measurement():
    feet = int(input("Enter your measurement in feet: "))
    one_feet_in_inches = 12
    one_feet_in_yards = 0.333333
    one_feet_in_miles = 0.000189394
    inches = one_feet_in_inches * feet
    yards = one_feet_in_yards * feet
    miles = one_feet_in_miles * feet
    print("\nYour %d feet measurement in: " % feet)
    print("inches will be %d" % inches)
    print("yards will be %.2f" % yards)
    print("miles will be %.4f" % miles)


#Results:
# Enter your measurement in feet: 234
# Your 234 feet measurement in:
# inches will be 2808
# yards will be 78.00
# miles will be 0.0443

