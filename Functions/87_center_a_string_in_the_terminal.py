"""
Write a function that takes a string of characters as its first parameter, and the width of
the terminal in characters as its second parameter. Your function should return a new
string that consists of the original string and the correct number of leading spaces
so that the original string will appear centered within the provided width when it is
printed. Do not add any characters to the end of the string. Include a main program
that demonstrates your function.
"""

WIDTH = 80


def center(s, width):
    if width < len(s):
        return s

    spaces = (width - len(s)) // 2
    result = " " * spaces + s

    return result


def main():
    print(center("A Famous Story", WIDTH))
    print(center("by:", WIDTH))
    print(center("Someone Famous", WIDTH))
    print()
    print("Once upon a time...")

if __name__ == '__main__':
    main()
