"""
Develop a program that reads a four-digit integer from the user and displays the sum
of the digits in the number. For example, if the user enters 3141 then your program
should display 3+1+4+1=9.
"""

# Read the input of the digits from the user
digits = input("Enter the 4-digit integer number: ")

# Convert to int each element of the string
dig1 = int(digits[0])
dig2 = int(digits[1])
dig3 = int(digits[2])
dig4 = int(digits[3])

# Compute the sum of the digits
sum_of_digits = dig1 + dig2 + dig3 + dig4

# Display the result
print("The sum of the digits in the number =", sum_of_digits)
