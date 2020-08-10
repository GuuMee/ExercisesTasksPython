"""
A line of best fit is a straight line that best approximates a collection of n data points.
In this exercise, we will assume that each point in the collection has an x coordinate
and a y coordinate. The symbols x¯ and y¯ are used to represent the average x value in
the collection and the average y value in the collection respectively. The line of best
fit is represented by the equation y = mx + b where m and b are calculated using
the following formulas:

m = (Sum( xy)−Sum(x)*Sum(y)/n) / (Sum(x^2)−(Sum(x))^2/n)
b = ¯y − m*x¯

Write a program that reads a collection of points from the user. The user will enter
the x part of the first coordinate on its own line, followed by the y part of the first
coordinate on its own line. Allow the user to continue entering coordinates, with the
x and y parts each entered on their own line, until your program reads a blank line for
the x coordinate. Display the formula for the line of best fit in the form y = mx + b
by replacing m and b with the values you calculated using the preceding formulas.
For example, if the user inputs the coordinates (1, 1), (2, 2.1) and (3, 2.9) then your
program should display y = 0.95x + 0.1.
"""


def best_fit(points):
    m = 0
    sum_x, sum_y = 0, 0
    sum_xy = 0
    x_avg, y_avg = 0,0
    length = len(points)
    for p in points:
        sum_xy += p[0]*p[1]
        sum_x += p[0]
        sum_y += p[1]
        sum_xy = round(sum_xy, 1)
    y_avg += sum_x / length
    x_avg += sum_y / length
    m += (sum_xy - (sum_x * sum_y)/length) / (sum_x**2 - (sum_x**2 / length))
    b = y_avg - (m * x_avg)
    print("The line of the best fit is y = %.2fx + %.2f" % (m, b))


def main():
    points = []
    i = 0
    length = 3
    # Read from user list of 2 point separated by space (alternate x,y = map(int, input())
    while i < length:
        inputs = list(map(float, input("Enter x and y followed by space (blank for quit): ").split()))
        points.append(inputs)
        i += 1
    best_fit(points)


if __name__ == '__main__':
    main()
