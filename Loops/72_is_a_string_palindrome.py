"""
A string is a palindrome if it is identical forward and backward. For example “anna”,
“civic”, “level” and “hannah” are all examples of palindromic words.Write a program
that reads a string from the user and uses a loop to determines whether or not it is a
palindrome. Display the result, including a meaningful output message.
"""

string = input("Enter a string: ")
is_palindrome = True

for i in range(0, len(string) // 2):
    if string[i] != string[len(string)-i-1]:
        is_palindrome = False

if is_palindrome:
    print(string, "is a palindrome")
else:
    print(string, "is not a palindrome")

