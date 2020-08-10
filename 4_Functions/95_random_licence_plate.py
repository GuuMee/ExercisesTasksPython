"""
In a particular jurisdiction, older license plates consist of three letters followed by
three numbers. When all of the license plates following that pattern had been used,
the format was changed to four numbers followed by three letters.
Write a function that generates a random license plate. Your function should have
approximately equal odds of generating a sequence of characters for an old license
plate or a new license plate. Write a main program that calls your function and
displays the randomly generated license plate.
"""
import re
from random import choice, randint

NUMBER_ZERO = 48
NUMBER_NINE = 58
LETTER_A = 65
LETTER_Z = 90


def rand_licence_plate(value):

    if value == 3:
        old_licence = ""

        for i in range(3):
            random_letter = chr(randint(LETTER_A, LETTER_Z))
            old_licence += random_letter
        for i in range(3):
            random_number = chr(randint(NUMBER_ZERO, NUMBER_NINE))
            old_licence += random_number
        return old_licence

    elif value == 4:
        new_licence = ""

        for i in range(4):
            random_number = chr(randint(NUMBER_ZERO, NUMBER_NINE))
            new_licence += random_number
        for i in range(3):
            random_letter = chr(randint(LETTER_A, LETTER_Z))
            new_licence += random_letter
        return new_licence


def main():
    value = int(input("Enter the value of style licence plate (old = 3, new = 4): " ))
    licence = rand_licence_plate(value)
    print("Your random Licence Plate is: ", licence)


if __name__ == '__main__':
    main()



