"""
While the popularity of cheques as a payment method has diminished in recent years,
some companies still issue them to pay employees or vendors. The amount being
paid normally appears on a cheque twice, with one occurrence written using digits,
and the other occurrence written using English words. Repeating the amount in two
different forms makes it much more difficult for an unscrupulous employee or vendor
to modify the amount on the cheque before depositing it.
In this exercise, your task is to create a function that takes an integer between 0 and
999 as its only parameter, and returns a string containing the English words for that
number. For example, if the parameter to the function is 142 then your function should
return “one hundred forty two”. Use one or more dictionaries to implement
your solution rather than large if/elif/else constructs. Include a main program that
reads an integer from the user and displays its value in English words.
"""


NUMBERS = {
    1: "one",     2: "two",    3: "three",     4: "four",
    5: "five",    6: "six",    7: "seven",    8: "eight",
    9: "nine",    10: "ten",   11: "eleven",     12: "twelve",
    13: "thirteen",     14: "fourteen",    15: "fifteen",
    16: "sixteen",    17: "seventeen",    18: "eighteen",
    19: "nineteen",    20: "twenty",    30: "thirty",
    40: "forty",    50: "fifty",    60: "sixty",    70: "seventy",
    80: "eighty",    90: "ninety",    100: "hundred"
}


def text_numbers(num):
    result = ""
    length = len(num)
    for k in NUMBERS:
        if length == 1 and k == int(num):
            result += NUMBERS[k]
            break
        elif length == 2:
            if int(num[0])*10 == k:
                result += NUMBERS[k]
                for k2 in NUMBERS:
                    if int(num[1]) == k2:
                        result += " " + NUMBERS[k2]
                        break
                break
        elif length == 3:
            if int(num[0]) == k:
                result += NUMBERS[k] + " " + NUMBERS[100]
                for k2 in NUMBERS:
                    if int(num[1])*10 == k2:
                        result += " " + NUMBERS[k2]
                        for k3 in NUMBERS:
                            if int(num[2]) == k3:
                                result += " " + NUMBERS[k3]
                                break
                                break

                break
    return result


def main():
    line = input("Enter the integer number from 0 - 999:")
    texted = text_numbers(line)
    print("Your number %s in texted version - %s" % (line, texted))


if __name__ == '__main__':
    main()
