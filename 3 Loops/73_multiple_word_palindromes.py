"""
There are numerous phrases that are palindromes when spacing is ignored. Examples
include “go dog”, “flee to me remote elf” and “some men interpret nine memos”,
among many others. Extend your solution to Exercise 72 so that it ignores spacing
while determining whether or not a string is a palindrome. For an additional challenge,
extend your solution so that is also ignores punctuation marks and treats uppercase
and lowercase letters as equivalent.
"""

string = input("Enter a string: ")
string_original = string

def is_palindrome(value):
    min = 0
    max = len(value) - 1

    # Scan string for letter equality at each end.
    # ... Move indexes closer to the center after each check.
    while True:

        # Return true if all characters were checked.
        if min > max:
            return True;

        a = value[min]
        b = value[max]

        # Return false is characters are not equal.
        if a != b:
            return False;

        # Move inwards.
        min += 1
        max -= 1

# Use to translate punctuation to spaces.
# ... Changes uppercase to lowercase.
diction = str.maketrans(",:.'!?ABCDEFGHIJKLMNOPQRSTUVWXYZ", "      abcdefghijklmnopqrtsuvwxyz")

# Change all punctuation to spaces.
string = string.translate(diction)

# Remove all spaces.
string = string.replace(" ", "")

# See if string is a palindrome.
if is_palindrome(string):
    print('"', string_original, '"', " - a palindrome")
else:
    print('"', string_original, '"', " - not a palindrome")

