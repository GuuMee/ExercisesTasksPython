"""
In this exercise you will create a function named nextPrime that finds and returns
the first prime number larger than some integer, n. The value of n will be passed to
the function as its only parameter. Include a main program that reads an integer from
the user and displays the first prime number larger than the entered value. Import
and use your solution to Exercise 92 while completing this exercise.
"""

from is_a_number_prime_92 import is_prime

def next_prime(n):
    n_next = n+1
    while not is_prime(n_next):
        n_next+=1
    return n_next

def main():
    value = int(input("Enter the integer:"))
    prime = is_prime
    if prime:
        print("Your Entered number %d is prime" % value)
        n_prime = next_prime(value)
        print("Next prime number will be %d" % n_prime)

    else:
        print("Number %d is not prime" % value)


if __name__ == '__main__':
    main()