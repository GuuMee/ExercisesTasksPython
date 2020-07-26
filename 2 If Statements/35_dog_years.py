"""
It is commonly said that one human year is equivalent to 7 dog years. However this
simple conversion fails to recognize that dogs reach adulthood in approximately two
years. As a result, some people believe that it is better to count each of the first two
human years as 10.5 dog years, and then count each additional human year as 4 dog
years.

Write a program that implements the conversion from human years to dog years
described in the previous paragraph. Ensure that your program works correctly for
conversions of less than two human years and for conversions of two or more human
years. Your program should display an appropriate error message if the user enters
a negative number.

"""

ONE_HUMAN_YEAR = 7
FIRST_TWO_HUMAN_YEARS = 10.5
ADDITIONAL_HUMAN_YEAR = 4

h_year = int(input("Enter the human year: "))
if h_year == 1:
    print("It will be", ONE_HUMAN_YEAR, "dog years")
elif h_year == 2:
    print("It will be", FIRST_TWO_HUMAN_YEARS, "dog years")
elif h_year > 2:
    h_year = h_year-2
    total = FIRST_TWO_HUMAN_YEARS + h_year * ADDITIONAL_HUMAN_YEAR
    print("It will be", total, "dog years")
elif h_year < 0:
    print("You entered the negative number")