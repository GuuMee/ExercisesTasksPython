"""
In a Canadian postal code, the first, third and fifth characters are letters while the
second, fourth and sixth characters are numbers. The province can be determined
from the first character of a postal code, as shown in the following table. No valid
postal codes currently begin with D, F, I, O, Q, U, W, or Z.
The second character in a postal code identifies whether the address is rural or
urban. If that character is a 0 then the address is rural. Otherwise it is urban.
Create a program that reads a postal code from the user and displays the province
associated with it, along with whether the address is urban or rural. For example,
if the user enters T2N 1N4 then your program should indicate that the postal code
is for an urban address in Alberta. If the user enters X0A 1B2 then your program
should indicate that the postal code is for a rural address in Nunavut or Northwest
Territories. Use a dictionary to map from the first character of the postal code to the
province name. Display a meaningful error message if the postal code begins with
an invalid character.
"""

PROVINCES = {
    "Newfoundland": "A",
    "Nova Scotia": "B",
    "Prince Edward Island": "C",
    "New Brunswick": "E",
    "Quebed": ["G", "H", "J"],
    "Ontario": ["K", "L", "M", "N", "P"],
    "Manitoba": "R",
    "Saskatchewan": "S",
    "Alberta": "T",
    "British Columbia": "V",
    "Nunavut": "X",
    "Northwest Territories": "X",
    "Yukon": "Y",
}

NO_WALID = ["D", "F", "I", "O", "Q", "U", "W", "Z"]


def identify_postal_code(string):
    province = ""
    address = ""
    for k in PROVINCES:
        for i in range(len(PROVINCES[k])):
            if string[0] == PROVINCES[k][i]:
                province += k + ", "
            elif string[0] in NO_WALID:
                province = "The postal code is invalid!"
            if string[1] == 0:
                address = "rural"
            else:
                address = "urban"
    province_new = province.replace(province[-2], "")
    return province_new, address


def main():
    print("Enter the postal code (e.g. T2N 1N4):")
    line = input()
    string = line.upper()
    province, address = identify_postal_code(string)

    print("It's %s address in %s" % (address, province))


if __name__ == '__main__':
    main()
