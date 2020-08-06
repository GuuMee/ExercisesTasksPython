"""
When analysing data collected as part of a science experiment it may be desirable
to remove the most extreme values before performing other calculations. Write a
function that takes a list of values and an non-negative integer, n, as its parameters.
The function should create a new copy of the list with the n largest elements and the
n smallest elements removed. Then it should return the new copy of the list as the
function’s only result. The order of the elements in the returned list does not have to
match the order of the elements in the original list.
Write a main program that demonstrates your function. Your function should read
a list of numbers from the user and remove the two largest and two smallest values
from it. Display the list with the outliers removed, followed by the original list. Your
program should generate an appropriate error message if the user enters less than 4
values.
"""

# Remove the outliers from a list of data
# @parm data the list of data values to process
# @param num_outliers the number of smallest and largest values to remove
# @return a new copy of data where the values are sorted into ascending order
# and the smallest and largest values have been removed


def remove_outliers(data, num_outliers):

    # Create a new copy of the list that is in sorted order
    ret_val = sorted(data)

    # Remove num_outliers largest values
    for i in range(num_outliers):
        ret_val.pop()

    # Remove num_outliers smallest values
    for i in range(num_outliers):
        ret_val.pop(0)

    # Return the result
    return ret_val


def main():

    # Read data from the user, and remove the two largest and two smallest values
    values = []
    s = input("Enter a value (blank line to quit): ")
    while s != "":
        num = float(s)
        values.append(num)
        s = input("Enter a value (blank line to quit): ")

        # Displays the result or an appropriate error message
        if len(values) < 4:
            print("You didn't enter enough values.")
        else:
            print("With the outliers removed: ", remove_outliers(values, 2))
            print("The original data: ", values)


if __name__ == '__main__':
    main()
