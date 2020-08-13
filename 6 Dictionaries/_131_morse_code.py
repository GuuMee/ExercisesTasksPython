"""
Morse code is an encoding scheme that uses dashes and dots to represent numbers
and letters. In this exercise, you will write a program that uses a dictionary to store
the mapping from letters and numbers to Morse code. Use a period to represent a dot,
and a hyphen to represent a dash. The mapping from letters and numbers to dashes
and dots is shown in Table 6.1.
Your program should read a message from the user. Then it should translate each
letter and number in the message to Morse code, leaving a space between each
sequence of dashes and dots. Your program should ignore any characters that are not
letters or numbers. The Morse code for Hello, World! is shown below:
.... . .-.. .-.. --- .-- --- .-. .-.. -..
Morse code was originally developed in the nineteenth century for use over
telegraph wires. It is still used today, over 160 years after it was first created.
"""

morse_alphabet = {
    "A": ".-",    "B": "-...",    "C": "-.-.",    "D": "-..",    "E": ".",
    "F": "..-.",   "G": "--.",    "H": "....",    "I": "..",
    "J": ".---",   "K": "-.-",    "L": ".-..",    "M": "--",    "N": "-.",
    "O": "---",    "P": ".--.",    "Q": "--.-",    "R": ".-.",
    "S": "...",    "T": "-",    "U": "..-",    "V": "...-",    "W": ".--",
    "X": "-..-",    "Y": "-.--",    "Z": "--..",
    0: "-----",    1: ".----",    2: "..---",    3: "...--",
    4: "....-",    5: ".....",    6: "-....",    7: "--...",
    8: "---..",    9: "----."
}
extra_characters = [".", ",", "?", "!", ":", " "]


def convert_to_morse(string):
    amount = ""

    for i in range(len(string)):
        item = string[i]
        if string[i] in extra_characters:
            new_string = string.replace(string[i], "")

    for i in range(len(new_string)):
        for j in morse_alphabet:
            is_in_alphabet = new_string[i] == j
            if is_in_alphabet:
                amount += " "+morse_alphabet[j]
                break
    return amount


def main():
    line = input("Enter the text or numbers: ")
    string = line.upper()
    converted = convert_to_morse(string)
    print("Your input converted to the Morse:")
    print(converted)


if __name__ == '__main__':
    main()
