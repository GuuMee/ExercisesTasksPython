"""
The year is divided into four seasons: spring, summer, fall and winter. While the
exact dates that the seasons change vary a little bit from year to year because of the
way that the calendar is constructed.

Create a program that reads a month and day from the user. The user will enter
the name of the month as a string, followed by the day within the month as an
integer. Then your program should display the season associated with the date
that was entered.
"""

SPRING = "March 20"
SUMMER = "June 21"
FALL = "September 22"
WINTER = "December 21"

month = input("Enter the name of the month: ")
day = int(input("Enter the day number: "))
season = ''

if month == "January" or month == "February":
    season = "Winter"
elif month == "March":
    if day < 20:
        season = "Winter"
    else:
        season = "Spring"
elif month == "April" or month == "May":
    season = "Spring"
elif month == "June":
    if day < 21:
        season = "Spring"
    else:
        season = "Summer"
elif month == "July" or month == "August":
    season = "Summer"
elif month == "September":
    if day < 22:
        season = "Summer"
    else:
        season = "Fall"
elif month == "October" or month == "November":
    season = "Fall"
elif month == "December":
    if day < 21:
        season = "Fall"
    else:
        season = "Winter"

print(month, day, "is in", season)