"""
Using your solutions to Exercises 94 and 96, write a program that generates a random
good password and displays it. Count and display the number of attempts that were
needed before a good password was generated. Structure your solution so that it
imports the functions you wrote previously and then calls them from a function
named main in the file that you create for this exercise.
"""

from random_94_password import random_password
from check_96_a_password import check_password


def random_good_password():
    password = random_password()
    print("Your random password:", password)
    if check_password(password):
        print("That's a good password.")
    else:
        print("That isn't a good password.")


def main():
    random_good_password()


if __name__ == '__main__':
    main()




