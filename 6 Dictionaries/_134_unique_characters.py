"""
Create a program that determines and displays the number of unique characters in a
string entered by the user. For example, Hello, World! has 10 unique characters
whilezzzhas only one unique character. Use a dictionary or set to solve this problem.
"""

# Compute the number of unique characters in a string using a dictionary

# Read the string from the user
s = input("Enter a string: ")

# Add each character to a dictionary with a value of True. Once we are done the number
# of keys in the dictionary will be number of unique characters  in the string.

characters = {}
for ch in s:
    characters[ch] = True

# Display the result
print("That string contained", len(characters), "unique character(s)")
