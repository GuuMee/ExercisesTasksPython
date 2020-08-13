"""
On some basic cell phones, text messages can be sent using the numeric keypad.
Because each key has multiple letters associated with it, multiple key presses are
needed for most letters. Pressing the number once generates the first letter on the
key. Pressing the number 2, 3, 4 or 5 times generates the second, third, fourth or fifth
character listed for that key.

Write a program that displays the key presses that must be made to enter a text
message read from the user. Construct a dictionary that maps from each letter or
symbol to the key presses. Then use the dictionary to generate and display the presses
for the user’s message. For example, if the user enters Hello, World! then your
program should output 4433555555666110966677755531111. Ensure that
your program handles both uppercase and lowercase letters. Ignore any characters
that aren’t listed in the table above such as semicolons and brackets.
"""

symbols = {
    1: [".", ",", "?", "!", ":"],
    2: ["a", "b", "c"],
    3: ["d", "e", "f"],
    4: ["g", "h", "i"],
    5: ["j", "k", "l"],
    6: ["m", "n", "o"],
    7: ["p", "q", "r", "s"],
    8: ["t", "u", "v"],
    9: ["w", "x", "y", "z"],
    0: [" "]
    }




def text_to_numbers(string):
    total = ""
    amount = ""
    for letter in string:
        for i in range(0, 10):
            for j in range(len(symbols[i])):
                nested_item = symbols[i][j]
                if symbols[i] == " ":
                    amount += "0"
                elif nested_item == letter:
                    times = j+1
                    amount = str(i) * times
        total += amount
    return total


def main():
    line = input("Enter the string: ")
    string = line.lower()
    numbers = text_to_numbers(string)
    print("Your entered text numbers converted to cellphone numbers:", numbers)


if __name__ == '__main__':
    main()
