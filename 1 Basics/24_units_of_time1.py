"""
Create a program that reads a duration from the user as a number of days, hours,
minutes, and seconds. Compute and display the total number of seconds represented
by this duration.

"""


def duration_unit():
    day_in_sec = 86400
    hour_in_sec = 3600
    minute_in_sec = 60
    days = int(input("Enter the duration numbers of days: "))
    hours = int(input("Enter the duration numbers of hours: "))
    mins = int(input("Enter the duration numbers of minutes: "))
    seconds = int(input("Enter the duration numbers of seconds: "))
    total = day_in_sec * days + hour_in_sec * hours + minute_in_sec * mins + seconds
    print("Total duration in seconds will be %d sec" % total)


# Results:
# Enter the duration numbers of days: 12
# Enter the duration numbers of hours: 23
# Enter the duration numbers of minutes: 10
# Enter the duration numbers of seconds: 18
# Total duration in seconds will be 1120218 sec
