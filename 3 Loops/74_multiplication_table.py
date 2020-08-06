"""
In this exercise you will create a program that displays a multiplication table that
shows the products of all combinations of integers from 1 times 1 up to and including
10 times 10. Your multiplication table should include a row of labels across the top
of it containing the numbers 1 through 10. It should also include labels down the left
side consisting of the numbers 1 through 10.
When completing this exercise you will probably find it helpful to be able to
print out a value without moving down to the next line. This can be accomplished
by added end="" as the last parameter to your print statement. For example,
print("A") will display the letter A and then move down to the next line. The
statement print("A", end="") will display the letter A without moving down
to the next line, causing the next print statement to display its result on the same line
as the letter A.
"""

MIN = 1
MAX = 10

print("    ", end="")

# Display the top row of labels
for i in range(MIN, MAX + 1):
    print("%4d" % i, end="")
print()

# Display the table
# Rows:
for i in range(MIN, MAX + 1):
    print("%4d" % i, end="")
    # Cells (Columns):
    for j in range(MIN, MAX + 1):
        print("%4d" % (i*j), end="")
    print()
