"""
An online retailer provides express shipping for many of its items at a rate of $10.95
for the first item, and $2.95 for each subsequent item. Write a function that takes the
number of items in the order as its only parameter. Return the shipping charge for
the order as the function’s result. Include a main program that reads the number of
items purchased from the user and displays the shipping charge.
"""
FIRST_ITEM = 10.95
SUBSEQUENT_ITEM = 2.95


def shipping_calculator(orders):
    charge = 0
    if orders == 1:
        charge += FIRST_ITEM
    else:
        orders -= 1
        charge += FIRST_ITEM
        while orders > 0:
            orders -= 1
            charge += SUBSEQUENT_ITEM

    print("The shipping charge for the order is $%.2f" % charge)

number = int(input("Enter the number of orders: "))

shipping_calculator(number)
