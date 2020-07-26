"""
In this exercise you will create a program that reads a letter of the alphabet from the
user. If the user enters a, e, i, o or u then your program should display a message
indicating that the entered letter is a vowel. If the user enters y then your program
should display a message indicating that sometimes y is a vowel, and sometimes y is
a consonant. Otherwise your program should display a message indicating that the
letter is a consonant.

"""
vowels = ['a', 'e', 'i','o', 'u']
letter = input("Enter the letter: ")

if letter in vowels:
    print("Your entered letter is vowel")
elif letter == 'y':
    print("The letter 'y' sometimes is a vowel, sometimes is a consonant")
else:
    print("The letter is a consonant")
