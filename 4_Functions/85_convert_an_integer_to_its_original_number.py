"""
Words like first, second and third are referred to as ordinal numbers. In this exercise,
you will write a function that takes an numeger as its only parameter and returns a
string containing the appropriate English ordinal number as its only result. Your
function must handle the numegers between 1 and 12 (inclusive). It should return an
empty string if a value outside of this range is provided as a parameter. Include a
main program that demonstrates your function by displaying each numeger from 1 to
12 and its ordinal number. Your main program should only run when your file has
not been imported numo another program.
"""


def integer_to_string(num):
    if num == 1:
        return "first"
    elif num == 2:
        return "second"
    elif num == 3:
        return "third"
    elif num == 4:
        return "fourth"
    elif num == 5:
        return "fifth"
    elif num == 6:
        return "sixth"
    elif num == 7:
        return "seventh"
    elif num == 8:
        return "eighth"
    elif num == 9:
        return "ninth"
    elif num == 10:
        return "tenth"
    elif num == 11:
        return "eleventh"
    elif num == 12:
        return "twelfth"


def main():
    number = int(input("Enter the integer number (from 1 - 12): "))
    string = integer_to_string(number)
    print("Your number's original - %s" % string)


if __name__ == '__main__':
    main()
