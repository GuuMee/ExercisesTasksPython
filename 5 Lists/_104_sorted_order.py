"""
Write a program that reads integers from the user and stores them in a list. Your
program should continue reading values until the user enters 0. Then it should display
all of the values entered by the user (except for the 0) in order from smallest to largest,
with one value appearing on each line. Use either the sort method or the sorted
function to sort the list.
"""

# Start with the empty list
data = []

# Read values, adding them to the list, until the user enters 0
num = int(input("Enter an integer (0 to quit):"))

while num != 0:
    data.append(num)
    num = int(input("Enter an integer (0 to quit): "))

# Sort the values
data.sort()

# Display he values in ascending order
print("The values, sorted ascending order, are: ")
for num in data:
    print(num)

