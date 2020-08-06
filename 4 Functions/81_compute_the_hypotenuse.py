"""
Write a function that takes the lengths of the two shorter sides of a right triangle as
its parameters. Return the hypotenuse of the triangle, computed using Pythagorean
theorem, as the function’s result. Include a main program that reads the lengths of
the shorter sides of a right triangle from the user, uses your function to compute the
length of the hypotenuse, and displays the result.

"""
a = 6
b = 9

def find_hypotenuse(a,b):
    c = (a**2 + b**2) * 0.5
    return c

hypotenuse = find_hypotenuse(a, b)

print("Hypotenuse is %.2f" % hypotenuse)



