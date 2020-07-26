"""
A triangle can be classified based on the lengths of its sides as equilateral, isosceles
or scalene. All 3 sides of an equilateral triangle have the same length. An isosceles
triangle has two sides that are the same length, and a third side that is a different
length. If all of the sides have different lengths then the triangle is scalene.
Write a program that reads the lengths of 3 sides of a triangle from the user.
Display a message indicating the type of the triangle.

"""

first_side = int(input("Enter the  first side of the triangle: "))
second_side = int(input("Enter the  second side of the triangle: "))
third_side = int(input("Enter the  third side of the triangle: "))

if first_side == second_side and second_side == third_side:
    print("This triangle is  EQUILATERAL")
elif first_side == second_side or second_side == third_side \
   or third_side == first_side:
    print("This triangle is ISOSCELES")
else:
    print("This triangle is SCALENE")
