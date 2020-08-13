"""
The notion of anagrams can be extended to multiple words. For example, “William
Shakespeare” and “I am a weakish speller” are anagrams when capitalization and
spacing are ignored.
Extend your program from Exercise 135 so that it is able to check if two phrases
are anagrams. Your program should ignore capitalization, punctuation marks and
spacing when making the determination.
"""


# Determine whether or not two strings are anagrams and report the result

# Compute the frequency distribution for the character in a string
# @param s the string to process
# @return a dictionary mapping each character to its count
def character_counts(s):
    # Create a new empty dictionary{}
    counts = {}
    # Update the count for each character in the string
    for ch in s:
        if ch in counts:
            coint_ch = counts[ch]
            counts[ch] = counts[ch] + 1
        else:
            counts[ch] = 1
    # Return the result
    return counts


# Determine if two strings entered by the user are anagrams
def main():
    # Read the strings from the user
    s1 = input("Enter  the first string: ")
    s2 = input("Enter the second string: ")

    # Delete all spaces of the string
    s1_spaces = s1.replace(" ", "")
    s2_spaces = s2.replace(" ", "")

    # Lower all the characters
    s1_lower = s1_spaces.lower()
    s2_lower = s2_spaces.lower()

    # Get the character counts for each string
    counts1 = character_counts(s1_lower)
    counts2 = character_counts(s2_lower)

    # Display the result
    if counts1 == counts2:
        print("Those strings are anagrams.")
    else:
        print("Those strings are not anagrams")


if __name__ == '__main__':
    main()
