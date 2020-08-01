"""
Exercise 51 included a table that shows the conversion from letter grades to grade
points at a particular academic institution. In this exercise you will compute the
grade point average of an arbitrary number of letter grades entered by the user. The
user will enter a blank line to indicate that all of the grades have been provided. For
example, if the user enters A, followed by C+, followed by B, followed by a blank
line then your program should report a grade point average of 3.1.
You may find your solution to Exercise 51 helpful when completing this exercise.
Your program does not need to do any error checking. It can assume that each value
entered by the user will always be a valid letter grade or a blank line.

"""

A = 4.0
A_MINUS = 3.7
B_PLUS = 3.3
B = 3.0
B_MINUS = 2.7
C_PLUS = 2.3
C = 2.0
C_MINUS = 1.7
D_PLUS = 1.3
D = 1.0
F = 0

sum_grades = 0
count = 0

grade_letter = input("Enter the grade letter: ")

while grade_letter != "":
    if grade_letter == "A++" or grade_letter == "A":
        sum_grades += A
    elif grade_letter == "A--":
        sum_grades += A_MINUS
    elif grade_letter == "B++":
        sum_grades += B_PLUS
    elif grade_letter == "B":
        sum_grades += B
    elif grade_letter == "B--":
        sum_grades += B_MINUS
    elif grade_letter == "C++":
        sum_grades += C_PLUS
    elif grade_letter == "C--":
        sum_grades += C_MINUS
    elif grade_letter == "D++":
        sum_grades += D_PLUS
    elif grade_letter == "D":
        sum_grades += D
    elif grade_letter == "F":
        sum_grades += F
    print("Sum grades", sum_grades)
    grade_letter = input("Enter the grade letter: (blank to quit): ")
    count += 1

average = sum_grades / (count)
print("The average grade of entered ones: %.2f" % average)

