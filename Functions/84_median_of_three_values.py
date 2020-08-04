"""
Write a function that takes three numbers as parameters, and returns the median value
of those parameters as its result. Include a main program that reads three values from
the user and displays their median.

Hint: The median value is the middle of the three values when they are sorted
into ascending order. It can be found using if statements, or with a little bit of
mathematical creativity.
"""


def median(a, b, c):
    if a < b < c or a > b > c:
        return b
    if b < a < c or b > a > c:
        return a
    if a < c < b or a > c > b:
        return c


def alternate_median(a, b, c):
    return a + b + c - min(a, b, c) - max(a, b, c)


def main():
    x = float(input("Enter the first value: "))
    y = float(input("Enter the second value: "))
    z = float(input("Enter the third value: "))

    print("The median values is: ", median(x, y, z))
    print("Using alternateive method, it is:", alternate_median(x, y, z))

main()
