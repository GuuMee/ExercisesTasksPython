"""
February 4, 2013 was the last day that pennies were distributed by the Royal Canadian
Mint. Now that pennies have been phased out retailers must adjust totals so that they
are multiples of 5 cents when they are paid for with cash (credit card and debit card
transactions continue to be charged to the penny). While retailers have some freedom
in how they do this, most choose to round to the closest nickel.
Write a program that reads prices from the user until a blank line is entered.
Display the total cost of all the entered items on one line, followed by the amount
due if the customer pays with cash on a second line. The amount due for a cash
payment should be rounded to the nearest nickel. One way to compute the cash
payment amount is to begin by determining how many pennies would be needed to
pay the total. Then compute the remainder when this number of pennies is divided
by 5. Finally, adjust the total down if the remainder is less than 2.5. Otherwise adjust
the total up.

"""

PENNIES_PER_NICKEL = 5
NICKEL = 0.05

total = 0.00
line = input("Enter the price of the item (blank to quit): ")

while line != "":
    total = total + float(line)
    # Read the cost of the next item
    line = input("Enter the price of the item (blank to quit): ")

print("The exact amount payable is %.02f" % total)

rounding_indicator = total * 100 % PENNIES_PER_NICKEL

if rounding_indicator < PENNIES_PER_NICKEL / 2:
    cash_total = total - rounding_indicator / 100
else:
    cash_total = total + NICKEL - rounding_indicator / 100
    print("The cash amount payable is %.02f" % cash_total)