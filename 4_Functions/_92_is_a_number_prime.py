"""
A prime number is an integer greater than 1 that is only divisible by one and itself.
Write a function that determines whether or not its parameter is prime, returning
True if it is, and False otherwise. Write a main program that reads an integer
from the user and displays a message indicating whether or not it is prime. Ensure
that the main program will not run if the file containing your solution is imported
into another program.
"""


def is_prime(n):
    if n <= 1:
        return False

    for i in range(2, n):

        # This below indicating that n is not prime
        if n % i == 0:
            return False
    return True


def main():
    value = int(input("Enter an integer: "))

    if is_prime(value):
        print(value, "is prime.")
    else:
        print(value, "is not prime.")


# Call the main function if the file has not been imported
if __name__ == '__main__':
    main()
