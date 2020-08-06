"""
An integer, n, is said to be perfect when the sum of all of the proper divisors of n is
equal to n. For example, 28 is a perfect number because its proper divisors are 1, 2,
4, 7 and 14, and 1 + 2 + 4 + 7 + 14 = 28.
Write a function that determines whether or not a positive integer is perfect. Your
function will take one parameter. If that parameter is a perfect number then your func�tion will return true. Otherwise it will return false. In addition, write a main program
that uses your function to identify and display all of the perfect numbers between 1
and 10,000. Import your solution to Exercise 109 when completing this task.
"""

from _109_list_of_proper_divisors import proper_divisors

LIMIT = 10000

# Determine whether or not a number is perfect. A number is perfect if the
# sum of its proper divisors is equal to the number itself
# @param 'n' the number  to check for perfection
# @return 'True' if the number is perfect, 'False' otherwise


def is_perfect_number(n):

    # Get a list of the proper divisors of n
    divisors = proper_divisors(n)

    # Compute the total of all of the divisors
    total = 0
    for d in divisors:
        total += d

    # Return the appropriate result
    if total == n:
        return True

    return False


# Display all of the perfect numbers between 1 and LIMIT
def main():
    print("The perfect numbers between 1 and", LIMIT,"are:")
    for i in range(1, LIMIT+1):
        if is_perfect_number(i):
            prop_divisor = proper_divisors(i)
            print(prop_divisor, " = ", i)


if __name__ == '__main__':
    main()