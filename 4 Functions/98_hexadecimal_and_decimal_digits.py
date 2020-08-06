"""
Write two functions, hex2int and int2hex, that convert between hexadecimal
digits (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E and F) and base 10 integers. The
hex2int function is responsible for converting a string containing a single hexadecimal
digit to a base 10 integer, while the int2hex function is responsible for converting
an integer between 0 and 15 to a single hexadecimal digit. Each function
will take the value to convert as its only parameter and return the converted value
as the function’s only result. Ensure that the hex2int function works correctly for
both uppercase and lowercase letters. Your functions should end the program with a
meaningful error message if an invalid parameter is provided.
"""
from ast import literal_eval


def hex2int(string):
    res = literal_eval(string)  # or res = int(string, 16)
    print("The decimal number of hexadecimal string : " + str(res))


def int2hex(number):
    res = float.hex(3.9)
    print("The hexadecimal form of %.2f is " % number, res)


def main():

    value = input("Select what do you want to convert. Hex to decimal(type 'h') or decimal to hex (d): ")
    if value == "h":
        to_decimal = input("Enter the hexadecimal number (0xAvb):")
        hex2int(to_decimal)
    elif value == "d":
        to_hex = float(input("Enter the decimal value:"))
        int2hex(to_hex)
    else:
        print("Your entered value is invalid. Try again...")


if __name__ == '__main__':
    main()
