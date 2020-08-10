"""
Many recipe books still use cups, tablespoons and teaspoons to describe the volumes
of ingredients used when cooking or baking. While such recipes are easy enough to
follow if you have the appropriate measuring cups and spoons, they can be difficult
to double, triple or quadruple when cooking Christmas dinner for the entire extended
family. For example, a recipe that calls for 4 tablespoons of an ingredient requires 16
tablespoons when quadrupled. However, 16 tablespoons would be better expressed
(and easier to measure) as 1 cup.
Write a function that expresses an imperial volume using the largest units possible.
The function will take the number of units as its first parameter, and the unit
of measure (cup, tablespoon or teaspoon) as its second parameter. Return a string
representing the measure using the largest possible units as the function’s only result.
For example, if the function is provided with parameters representing 59 teaspoons
then it should return the string “1 cup, 3 tablespoons, 2 teaspoons”.

Hint: One cup is equivalent to 16 tablespoons. One tablespoon is equivalent to
3 teaspoons.
"""

# Reduce an imperial measurement so that it is expressed using the largest possible
# units of measure

ONCE_CUP = 16  # tablespoons
ONE_TABLESPOON = 3  # teaspoons


# Reduce an imperial measurement so that it is expressed using the largest possible
# units of measure
# @param 'num' the number of units that need to be reduced
# @param 'unit' the unit of measure (cup, tablespoon, teaspoon)
# @return a string representing the measurement in reduced form
def reduce_measure(num, unit):
    unit = unit.lower()
    teaspoons = 0
    if unit == "teaspoon" or unit == "teaspoons":
        teaspoons = num
    elif unit == "tablespoon" or unit == "tablespoons":
        teaspoons = num * ONE_TABLESPOON
    elif unit == "cup" or "cups":
        teaspoons = num * ONCE_CUP

    # Convert the number of teaspoons to the largest possible units of measure
    cups = teaspoons // ONCE_CUP
    teaspoons -= cups * ONCE_CUP
    tablespoons = teaspoons // ONE_TABLESPOON
    teaspoons -= tablespoons * ONE_TABLESPOON

    # Generate the result string
    result = ""

    # Add the number of cups to the result string(if any)
    if cups > 0:
        result += str(cups) + " cup"
        if cups > 1:
            result += "s"

    # Add the number of tablespoons to the result string(if any)
    if tablespoons > 0:

        # Include a comma if there were some cups
        if result != "":
            result += ", "

        result += str(tablespoons) + " tablespoon"
        if tablespoons > 1:
            result += "s"

    # Add the number of teaspoons to the result string(if any)
    if teaspoons > 0:

        # Include a comma if there were some cups and/or tablespoons
        if result != "":
            result += ","

        result += str(teaspoons) + " teaspoon"
        if teaspoons > 1:
            result += "s"

    # Handle the case where the number of units was 0
    if result == "":
        result = "0 teaspoons"

    return result


# Demonstrate the reduce_measure() function by performing several reductions
def main():
    print("59 teaspoons is %s." % reduce_measure(59, "teaspoons"))
    print("59 tablespoons is %s." % reduce_measure(59, "tablespoons"))
    print("1 teaspoon is %s." % reduce_measure(1, "teaspoon"))
    print("1 tablespoon is %s." % reduce_measure(1, "tablespoon"))
    print("1 cup is %s." % reduce_measure(1, "cup"))
    print("4 cups is %s." % reduce_measure(4, "cups"))
    print("3 teaspoons is %s." % reduce_measure(3, "teaspoons"))
    print("3 teaspoons is %s." % reduce_measure(3, "teaspoons"))
    print("3 teaspoons is %s." % reduce_measure(3, "teaspoons"))
    print("6 teaspoons is %s." % reduce_measure(6, "teaspoons"))
    print("95 teaspoons is %s." % reduce_measure(95, "teaspoons"))
    print("96 teaspoons is %s." % reduce_measure(96, "teaspoons"))
    print("97 teaspoons is %s." % reduce_measure(97, "teaspoons"))
    print("98 teaspoons is %s." % reduce_measure(98, "teaspoons"))
    print("99 teaspoons is %s." % reduce_measure(99, "teaspoons"))


if __name__ == '__main__':
    main()