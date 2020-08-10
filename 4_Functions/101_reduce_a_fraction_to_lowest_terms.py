"""
Write a function that takes two positive integers that represent the numerator and
denominator of a fraction as its only two parameters. The body of the function
should reduce the fraction to lowest terms and then return both the numerator and
denominator of the reduced fraction as its result. For example, if the parameters
passed to the function are 6 and 63 then the function should return 2 and 21. Include
a main program that allows the user to enter a numerator and denominator. Then
your program should display the reduced fraction.

Hint: In Exercise 75 you wrote a program for computing the greatest common
divisor of two positive integers. You may find that code useful when completing
this exercise.
"""


# Compute the greatest common divisor of two integers
def gcd(n, m):
    # Initialize d to the smallest of n and m
    d = min(n, m)

    # Use a while loop to find the greatest common divisor of n and m
    while n % d != 0 or m % d != 0:
        d -= 1

    return d


def reduce(num, den):
    # If numerator is 0 then the reduced fraction in 0/1
    if num == 0:
        return (0, 1)

    g = gcd(num, den)

    # Divide both the numerator and denominator by the gcd and return the result
    return (num // g, den // g)


# Read the fraction from the user and display the reduced fraction
def main():
    num = int(input("Enter the numerator: "))
    den = int(input("Enter the denominator: "))

    # Compute the reduced fraction
    (n, d) = reduce(num, den)

    # Display the result
    print(" %d/%d can be reduced to %d/%d." % (num, den, n, d))


if __name__ == '__main__':
    main()





