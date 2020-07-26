"""
In the previous question you converted from note name to frequency. In this question
you will write a program that reverses that process. Begin by reading a frequency
from the user. If the frequency is within one Hertz of a value listed in the table in
the previous question then report the name of the note. Otherwise report that the
frequency does not correspond to a known note. In this exercise you only need to
consider the notes listed in the table. There is no need to consider notes from other
octaves.

"""

C4 = 261.63
D4 = 293.66
E4 = 329.63
F4 = 349.23
G4 = 392.00
A4 = 440.00
B4 = 493.88
LIMIT = 1

freq = float(input("Enter a frequency: "))

if C4 - LIMIT <= freq <= C4 + LIMIT:
    note = "C4"
elif D4 - LIMIT <= freq <= D4 + LIMIT:
    note = "D4"
elif E4 - LIMIT <= freq <= E4 + LIMIT:
    note = "E4"
elif F4 - LIMIT <= freq <= F4 + LIMIT:
    note = "F4"
elif G4 - LIMIT <= freq <= G4 + LIMIT:
    note = "G4"
elif A4 - LIMIT <= freq <= A4 + LIMIT:
    note = "A4"
elif B4 - LIMIT <= freq <= B4 + LIMIT:
    note = "B4"
else:
    note = ""

if note == "":
    print("There is no note that corresponds to that frequency.")
else:
    print("That frequency is", note)