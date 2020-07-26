"""
The length of a month varies from 28 to 31 days. In this exercise you will create
a program that reads the name of a month from the user as a string. Then your
program should display the number of days in that month. Display “28 or 29 days”
for February so that leap years are addressed.

"""

month = input("Enter the hole month (like: February): ")

days = 31

if month == "April" or month == "June" or month == "September" or month == "November":
    days = 30
elif month == "February":
    days = "28 or 29"

print(month, "has", days, "days in it.")