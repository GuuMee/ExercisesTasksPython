"""
Pig Latin is a language constructed by transforming English words. While the ori�gins of the language are unknown, it is mentioned in at least two documents from
the nineteenth century, suggesting that it has existed for more than 100 years. The
following rules are used to translate English into Pig Latin:
• If the word begins with a consonant (including y), then all letters at the beginning of
the word, up to the first vowel (excluding y), are removed and then added to the end
of the word, followed by ay. For example, computer becomes omputercay
and think becomes inkthay.
• If the word begins with a vowel (not including y), then way is added to the end
of the word. For example, algorithm becomes algorithmway and office
becomes officeway.
Write a program that reads a line of text from the user. Then your program should
translate the line into Pig Latin and display the result. You may assume that the string
entered by the user only contains lowercase letters and spaces.
"""
vowels = ["a", "e", "i", "o", "u"]


def pig_latin(s):
    length = len(s)
    if s[0] not in vowels:
        if s[1] not in vowels:
            if s[2] not in vowels:
                removed = s[0:3]
                changed = s[3:length+1]+removed+"ay"
                return changed
            removed = s[0:2]
            changed = s[2:length + 1] + removed + "ay"
            return changed
        removed = s[0:1]
        changed = s[1:length + 1] + removed + "ay"
        return changed
    elif s[0] in vowels:
        changed = s + "way"
        return changed


def main():
    line = input("Enter the line of the text: ")
    p_latin = pig_latin(line)
    print("The result of the translated text to pig latin:", p_latin)


if __name__ == '__main__':
    main()
