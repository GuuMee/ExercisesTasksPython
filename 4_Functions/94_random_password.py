"""
Write a function that generates a random password. The password should have a
random length of between 7 and 10 characters. Each character should be randomly
selected from positions 33 to 126 in the ASCII table. Your function will not take
any parameters. It will return the randomly generated password as its only result.
Display the randomly generated password in your file’s main program. Your main
program should only run when your solution has not been imported into another file.

Hint: You will probably find the chr function helpful when completing this
exercise. Detailed information about this function is available online.
"""

from random import randint

SHORTEST = 7
LONGEST = 10
MIN_ASCII = 33
MAX_ASCII = 126


def random_password():
    random_length = randint(SHORTEST, LONGEST)

    result = ""
    for i in range(random_length):
        random_char = chr(randint(MIN_ASCII, MAX_ASCII))
        # chr() takes an ASCII code as its parameter. It returns a string containing the
        # character with that ASCII code as its result

        result += random_char
    return result


def main():
    print("Your random password is:", random_password())


if __name__ == '__main__':
    main()

