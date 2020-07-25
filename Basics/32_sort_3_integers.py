"""
Create a program that reads three integers from the user and displays them in sorted
order (from smallest to largest). Use the min and max functions to find the smallest
and largest values. The middle value can be found by computing the sum of all three
values, and then subtracting the minimum value and the maximum value.
"""

# Sort 3 values by the user into increasing order

# Read the numbers from the user, naming them a, b, c
a = int(input("Enter the first integer number: "))
b = int(input("Enter the second integer number: "))
c = int(input("Enter the third integer number: "))

mn = min(a, b, c)          # the minimum value
mx = max(a, b, c)          # the maximum value
md = a + b + c - mn - mx   # the middle value

# Display the result
print("The numbers in sorted order are: ")
print(" ", mn)
print(" ", md)
print(" ", mx)
