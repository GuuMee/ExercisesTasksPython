"""
Write a program that reads a date from the user and computes its immediate successor.
For example, if the user enters values that represent 2013-11-18 then your program
should display a message indicating that the day immediately after 2013-11-18 is
2013-11-19. If the user enters values that represent 2013-11-30 then the program
should indicate that the next day is 2013-12-01. If the user enters values that represent
2013-12-31 then the program should indicate that the next day is 2014-01-01. The
date will be entered in numeric form with three separate input statements; one for
the year, one for the month, and one for the day. Ensure that your program works
correctly for leap years.

"""
months_31 = [1, 3, 5, 7, 8, 10]
months_30 = [2, 4, 6, 9, 11]

year = int(input("Enter the year: "))
month = int(input("Enter the month: "))
day = int(input("Enter the day: "))

if year % 400 == 0:
    isLeapYear = True
elif year % 100 == 0:
    isLeapYear = False
elif year % 4 == 0:
    isLeapYear = True
else:
    isLeapYear = False

if isLeapYear and month == 2 and day == 28:
    day += 1
elif isLeapYear and month == 2 and day == 29 or not isLeapYear and month == 2 and day == 28:
    day = 1
    month = 3
elif month in months_31 and day == 31 or month in months_30 and day == 30:
    day = 1
    month += 1
elif month == 12 and day == 31:
    year += 1
    month = 1
    day = 1
elif day < 30:
    day += 1

print(day, "-", month, "-", year)
