"""
A bakery sells loaves of bread for $3.49 each. Day old bread is discounted by 60
percent. Write a program that begins by reading the number of loaves of day old
bread being purchased from the user. Then your program should display the regular
price for the bread, the discount because it is a day old, and the total price. All of the
values should be displayed using two decimal places, and the decimal points in all
of the numbers should be aligned when reasonable values are entered by the user.
"""

# Compute the price of a day old bread order

BREAD_PRICE = 3.49
DISCOUNT_RATE = 0.60

# Read the number of loaves from the user
num_loaves = int(input("Enter the number of day loaves: "))

# Compute the discount and total price
regular_price = num_loaves * BREAD_PRICE
discount = regular_price * DISCOUNT_RATE
total = regular_price - discount

# Display the result
print("Regular price: %5.2f" % regular_price)
print("Discount: %5.2f" % discount)
print("Total: %5.2f" % total)

