"""
A particular zoo determines the price of admission based on the age of the guest.
Guests 2 years of age and less are admitted without charge. Children between 3 and
12 years of age cost $14.00. Seniors aged 65 years and over cost $18.00. Admission
for all other guests is $23.00.
Create a program that begins by reading the ages of all of the guests in a group
from the user, with one age entered on each line. The user will enter a blank line to
indicate that there are no more guests in the group. Then your program should display
the admission cost for the group with an appropriate message. The cost should be
displayed using two decimal places.
"""

BABY_PRICE = 0.00
CHILD_PRICE = 14.00
ADULT_PRICE = 23.00
SENIOR_PRICE = 18.00

BABY_LIMIT = 2
CHILD_LIMIT = 12
ADULT_LIMIT = 64

total = 0

line = input("Enter the age of the guest: ")

while line != "":
    age = int(line)

    if age <= BABY_LIMIT:
        total += BABY_PRICE
    elif age <= CHILD_LIMIT:
        total += CHILD_PRICE
    elif age <= ADULT_LIMIT:
        total += ADULT_PRICE
    else:
        total += SENIOR_PRICE

    line = input("Enter the age of the guest (blank to finish): ")

print("The total for that group in $%.2f" % total)

