"""
Write a program that reads a month and day from the user. If the month and day
match one of the holidays listed previously then your program should display the
holiday’s name. Otherwise your program should indicate that the entered month and
day do not correspond to a fixed-date holiday.
"""

NEW_YEAR = 'January 1'
PROGRAMMERS = 'January 7'
SICK = "February 11"

CANADA_AY = 'July 1'



month_day = input("Enter the month and the day to figure out fixed-date holiday (e.g. 'January 1'): ")

if month_day == NEW_YEAR:
    holiday = "It's a New Year!"
    print("Happy Holiday!", holiday)
elif month_day == SICK:
    holiday = "It's World Day of the Sick!"
    print("Happy Holiday!", holiday)
elif month_day == CANADA_AY:
    holiday = "It's a Canada Day!"
    print("Happy Holiday!", holiday)
else:
    holiday = "Entered moth and day not correspond to a fixed-date holiday"
    print(holiday)



