"""
Write a program that reads numbers from the user until a blank line is entered. Your
program should display the average of all of the values entered by the user. Then
the program should display all of the below average values, followed by all of the
average values (if any), followed by all of the above average values. An appropriate
label should be displayed before each list of values.
"""


def average(list):
    avg = 0
    total = 0
    length = len(list)
    for i in range(1, length):
        total += list[i]
        avg = total / length
    return avg


def main():
    ls = []
    value = int(input("Enter the number (blank to quit): "))
    while value:
        ls.append(value)
        avg = average(ls)
        print("Your list:", ls)
        print("The average of the numbers:", avg)
        value = int(input("Enter the number (blank to quit): "))


if __name__ == '__main__':
    main()