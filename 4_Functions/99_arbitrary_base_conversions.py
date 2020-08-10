"""
Write a program that allows the user to convert a number from one base to another.
Your program should support bases between 2 and 16 for both the input number and
the result number. If the user chooses a base outside of this range then an appropriate
error message should be displayed and the program should exit. Divide your program
into several functions, including a function that converts from an arbitrary base to
base 10, a function that converts from base 10 to an arbitrary base, and a main
program that reads the bases and input number from the user. You may find your
solutions to Exercises 77, 78 and 98 helpful when completing this exercise.
"""

from hexadecimal_98_and_decimal_digits import hex2int, int2hex


# Convert a number from base 10 to base n
def dec2n(num, new_base):
    result = ""
    q = num

    # Perform the body of the loop once
    r = q % new_base
    result += int2hex(r)
    q //= new_base

    # Continue looping until q == 0
    while q > 0:
        r = q % new_base
        result += int2hex(r)
        q //= new_base

    return result


# Convert a number from base b to base 10
def n2dec(num, b):
    decimal = 0
    power = 0

    # Process each digit in the base b number
    for i in range(len(num)):
        decimal *= b
        decimal = decimal + hex2int(num[i])

    return decimal


def main():

    # Read the number from the user
    from_base = int(input("Enter the base to convert from:"))
    from_num = input("Enter a sequence of digits in that base: ")

    # Convert to base 10 and display the result
    dec = n2dec(from_num, from_base)
    print("That's %d in base 10." % dec)

    # Convert to a new base and display the resule
    to_base = int(input("Enter the base to convert to: "))
    to_num = dec2n(dec, to_base)
    print("That's %s in base %d." % (to_num, to_base))


if __name__ == '__main__':
    main()


# OTHER SOLUTIONS:

# divides longnum src (in base src_base) by divisor
# returns a pair of (longnum dividend, remainder)
def divmod_long(src, src_base, divisor):
    dividend = []
    remainder = 0
    for d in src:
        (e, remainder) = divmod(d + remainder * src_base, divisor)
        if dividend or e: dividend += [e]
    return (dividend, remainder)


def convert(src, src_base, dst_base):
    result = []
    while src:
        (src, remainder) = divmod_long(src, src_base, dst_base)
        result = [remainder] + result
    return result
