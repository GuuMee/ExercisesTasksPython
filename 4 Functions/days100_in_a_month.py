"""
Write a function that determines how many days there are in a particular month. Your
function will take two parameters: The month as an integer between 1 and 12, and
the year as a four digit integer. Ensure that your function reports the correct number
of days in February for leap years. Include a main program that reads a month and
year from the user and displays the number of days in that month. You may find your
solution to Exercise 57 helpful when solving this problem.
"""
months_31 = [1, 3, 5, 7, 8, 10, 12]
months_30 = [2, 4, 6, 9, 11]


def leap_year(year):

    is_leap_year = ''
    if year % 400 == 0:
        is_leap_year = True
    elif year % 100 == 0:
        is_leap_year = False
    elif year % 4 == 0:
        is_leap_year = True
    else:
        is_leap_year = False

    return is_leap_year


def days_in_month(month, year):
    days = 0
    if month in months_31:
        days = 31
    if month in months_30:
        days = 30

    if leap_year(year):
        if month == 2:
            days = 29
    else:
        if month == 2:
            days = 28

    return days


def main():
    year = int(input("Enter the year (4 digits): "))
    month = int(input("Enter the month's number (1-12): "))
    days = days_in_month(month, year)
    print("There're %d days" % days)


if __name__ == '__main__':
    main()

    
    