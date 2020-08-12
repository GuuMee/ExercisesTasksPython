"""
Write a function named reverseLookup that finds all of the keys in a dictionary
that map to a specific value. The function will take the dictionary and the value to
search for as its only parameters. It will return a (possibly empty) list of keys from
the dictionary that map to the provided value.
Include a main program that demonstrates the reverseLookup function as part
of your solution to this exercise. Your program should create a dictionary and then
show that the reverseLookup function works correctly when it returns multiple
keys, a single key, and no keys. Ensure that your main program only runs when
the file containing your solution to this exercise has not been imported into another
program.
"""


def reverse_lookup(data, value):
    keys = []

    for key in data:
        if data[key] == value:
            keys.append(key)
    return keys

def main():
    fr_en = {"le": "the", "la": "the", "livre": "book", "pomme": "apple"}

    print("The french words for 'the' are:", reverse_lookup(fr_en, "the"))
    print("Expected: ['le', 'la']")
    print()
    print("The french words for 'apple' are:", reverse_lookup(fr_en, "apple"))
    print("Expected: ['pomme']")
    print()
    print("The french words for 'asdf' are:", reverse_lookup(fr_en, "asdf"))
    print("Expected: []")
    print()


if __name__ == '__main__':
    main()
