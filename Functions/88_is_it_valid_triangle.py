"""
If you have 3 straws, possibly of differing lengths, it may or may not be possible
to lay them down so that they form a triangle when their ends are touching. For
example, if all of the straws have a length of 6 inches. then one can easily construct
an equilateral triangle using them. However, if one straw is 6 inches. long, while the
other two are each only 2 inches. long, then a triangle cannot be formed. In general,
if any one length is greater than or equal to the sum of the other two then the lengths
cannot be used to form a triangle. Otherwise they can form a triangle.
Write a function that determines whether or not three lengths can form a triangle.
The function will take 3 parameters and return a Boolean result. In addition, write a
program that reads 3 lengths from the user and demonstrates the behaviour of this
function.
"""


def valid_triangle(a, b, c):

    if (a + b > c) and (a + c > b) and (c + b > a):
        return True
    else:
        return False


def type_triangle(a, b, c):
    if (a**2 + b**2) == c**2 or (a**2 + c**2) == b**2 or c**2 + b**2 == a**2:
        return print("This is a right triangle")  # прямоугольный
    elif a == b and a != c or a == c and a != b or b == c and b != a:
        return print("This is an isosceles triangle")  # равнобедренный
    elif a == c and c == b:
        return print("This is an equilateral triangle")  # равносторонний
    elif (a + b > c) and (a + c > b) and (c + b > a):
        print("Triangle is just possible")


def main():
    a = int(input("Enter the 1st length: "))
    b = int(input("Enter the 2nd length: "))
    c = int(input("Enter the 3rd length: "))

    if valid_triangle(a, b, c):
        print("Triangle is valid with entered lengths:", end=" ")
        type_triangle(a, b, c)
    else:
        print("Triangle is impossible")


if __name__ == '__main__':
    main()
