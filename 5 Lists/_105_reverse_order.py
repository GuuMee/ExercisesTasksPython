"""
Write a program that reads integers from the user and stores them in a list. Use 0 as
a sentinel value to mark the end of the input. Once all of the values have been read
your program should display them (except for the 0) in reverse order, with one value
appearing on each line.
"""


# Start with the empty list
data = []

# Read values, adding them to the list, until the user enters 0
num = int(input("Enter an integer (0 to quit):"))

while num != 0:
    data.append(num)
    num = int(input("Enter an integer (0 to quit): "))

# Sort the values
desc = sorted(data, reverse=True)

# Display he values in ascending order
print("The values, sorted ascending order, are: ")
for num in desc:
    print(num)
