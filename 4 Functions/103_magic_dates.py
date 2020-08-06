"""
A magic date is a date where the day multiplied by the month is equal to the two digit
year. For example, June 10, 1960 is a magic date because June is the sixth month, and
6 times 10 is 60, which is equal to the two digit year. Write a function that determines
whether or not a date is a magic date. Use your function to create a main program
that finds and displays all of the magic dates in the 20th century. You will probably
find your solution to Exercise 100 helpful when completing this exercise.
"""


from days100_in_a_month import days_in_month


def is_magic_date(day, month, year):
    magic = day * month == year % 100
    if magic:
        return True

    return False


def main():
    for year in range(1900, 2021):
        for month in range(1, 13):
            for day in range(1, days_in_month(month, year) + 1):
                if is_magic_date(day, month, year):
                    print("%02d/%02d/%04d is a magic date." % (day, month, year))


if __name__ == '__main__':
    main()

