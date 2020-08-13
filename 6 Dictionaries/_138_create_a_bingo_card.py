"""
A Bingo card consists of 5 columns of 5 numbers. The columns are labeled with the
letters B, I, N, G and O. There are 15 numbers that can appear under each letter. In
particular, the numbers that can appear under the B range from 1 to 15, the numbers
that can appear under the I range from 16 to 30, the numbers that can appear under
the N range from 31 to 45, and so on.
Write a function that creates a random Bingo card and stores it in a dictionary. The
keys will be the letters B, I, N, G and O. The values will be the lists of five numbers
that appear under each letter. Write a second function that displays the Bingo card
with the columns labeled appropriately. Use these functions to write a program tha
displays a random Bingo card. Ensure that the main program only runs when the file
containing your solution has not been imported into another program.

You may be aware that Bingo cards often have a “free” space in the middle of
the card. We won’t consider the free space in this exercise.
"""

# Create and display the random bingo card

from random import randrange

NUMS_PER_LETTER = 15

# Create a bingo card with randomly generated numbers
# @return a dictionary representing the card where the keys are the strings
# "B", "I", "N", "G", "O", and the values are lists of the
# numbers that appear under each letter from top to bottom

def create_card():
    card = {}

    # The range of integers that can be generated for the current letter
    lower = 1
    upper = 1 + NUMS_PER_LETTER

    # For each of the five letters
    for letter in ["B", "I", "N", "G", "O"]:
        # Start witj an empty list for the letter
        card[letter] = []
        while len(card[letter]) != 5:
            next_num = randrange(lower, upper)
            # Ensure that we do not include any duplicate numbers
            if next_num not in card[letter]:
                card[letter].append(next_num)

        # Update the range of values that will be generated for the next letter
        lower += NUMS_PER_LETTER
        upper += NUMS_PER_LETTER

    # Return the generated card
    return card


# Display a bingo card with nice formatting
# @param card the bingo card to display
# @return (None)
def display_card(card):

    # Display the headings
    print("B  I  N  G  O")

    # Display the numbers on the card
    for i in range(5):
        for letter in ["B", "I", "N", "G", "O"]:
            print("%2d " % card[letter][i], end = "")
        print()


def main():
    card = create_card()
    display_card(card)


if __name__ == '__main__':
    main()