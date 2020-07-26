"""
It is common for images of a country’s previous leaders, or other individuals of historical
significance, to appear on its money. The individuals that appear on banknotes
in the United States are listed in Table 2.1.
Write a program that begins by reading the denomination of a banknote from the
user. Then your program should display the name of the individual that appears on the banknote of the entered amount.
An appropriate error message should be displayed if no such note exists.

While two dollar banknotes are rarely seen in circulation in the United States,
they are legal tender that can be spent just like any other denomination. The
United States has also issued banknotes in denominations of $500, $1,000,
$5,000, and $10,000 for public use. However, high denomination banknotes
have not been printed since 1945 and were officially discontinued in 1969. As
a result, we will not consider them in this exercise.

"""

GEORGE_WASHINGTON = 1
THOMAS_JEFFERSON = 2
ABRAHAM_LINCOLN = 5
ALEXANDER_HAMILTON = 10
ANDREW_JACKSON = 20
ULYSSES_S_GRANT = 50
BENJAMIN_FRANKLIN = 100

banknote = int(input("Enter the denomination of the banknote (in digits): "))

if banknote == 1:
    print("The individual that appears on the banknote $1 is George Washington")
elif banknote == 2:
    print("The individual that appears on the banknote $2 is Thomas Jefferson")
elif banknote == 5:
    print("The individual that appears on the banknote $5 is Abraham Lincoln ")
elif banknote == 10:
    print("The individual that appears on the banknote $10 is Alexander Hamilton")
elif banknote == 20:
    print("The individual that appears on the banknote $20 is Andrew Jackson")
elif banknote == 50:
    print("The individual that appears on the banknote $50 is Ulysses S. Grant")
elif banknote == 100:
    print("The individual that appears on the banknote $100 is Benjamin Franklin")
elif banknote > 100 :
    print(" The high denomination banknotes have not been printed since 1945 and were officially discounted in 1969")
else:
    print("Error! There's no banknote denomination!")