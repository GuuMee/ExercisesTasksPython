"""
Extend your solution to Exercise 115 so that it correctly handles uppercase letters and
punctuation marks such as commas, periods, question marks and exclamation marks.
If an English word begins with an uppercase letter then its Pig Latin representation
should also begin with an uppercase letter and the uppercase letter moved to the end of
the word should be changed to lowercase. For example, Computer should become
Omputercay. If a word ends in a punctuation mark then the punctuation mark
should remain at the end of the word after the transformation has been performed.
For example, Science! should become Iencescay!.
"""

vowels = ["a", "e", "i", "o", "u"]
punctuations = [".", ",", "!", "?", '"']


def pig_latin(s):
    length = len(s)
    if s[-1] not in punctuations:
        if s[0] not in vowels:
            if s[1] not in vowels:
                if s[2] not in vowels:
                    lov1 = s[0].lower()
                    removed = lov1+s[1:3]
                    changed = s[3].upper() + s[4:length-1]+removed+"ay"
                    return changed
                lov1 = s[0].lower()
                removed = lov1 + s[1:2]
                changed = s[2].upper() + s[3:length - 1] + removed + "ay"
                return changed
            lov1 = s[0].lower()
            removed = lov1
            changed = s[1].upper() + s[2:length - 1] + removed + "ay"
            return changed
        elif s[0] in vowels:
            changed = s + "way"
            return changed
    elif s[-1] in punctuations:
        if s[0] not in vowels:
            if s[1] not in vowels:
                if s[2] not in vowels:
                    lov1 = s[0].lower()
                    removed = lov1 + s[1:3]
                    changed = s[3].upper() + s[4:length - 1] + removed + "ay" + s[-1]
                    return changed
                lov1 = s[0].lower()
                removed = lov1 + s[1:2]
                changed = s[2].upper() + s[3:length - 1] + removed + "ay" + s[-1]
                return changed
            lov1 = s[0].lower()
            removed = lov1
            changed = s[1].upper() + s[2:length - 1] + removed + "ay" + s[-1]
            return changed
        elif s[0] in vowels:
            changed = s[0:length-1] + "way" + s[-1]
            return changed


def main():
    line = input("Enter the line of the text: ")
    p_latin = pig_latin(line)
    print("The result of the translated text to pig latin:", p_latin)


if __name__ == '__main__':
    main()
