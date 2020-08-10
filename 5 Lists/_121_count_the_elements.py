"""
Python’s standard library includes a method named count that determines how
many times a specific value occurs in a list. In this exercise, you will create a new
function named countRange which determines and returns the number of elements
within a list that are greater than or equal to some minimum value and less than some
maximum value. Your function will take three parameters: the list, the minimum
value and the maximum value. It will return an integer result greater than or equal to
0. Include a main program that demonstrates your function for several different lists,
minimum values and maximum values. Ensure that your program works correctly
for both lists of integers and lists of floating point numbers.
"""


# Determine how many elements in data are greater than or equal to mn and less than mx
# @param data - the list to process
# @param mn the minimum acceptable value
# @param mx the exclusive upper bound on acceptability
# @return the number of elements, e, such that mn <= e < mx
def count_range(data, mn, mx):
    # Count the number of elements within the acceptable range
    count = 0
    for e in data:
        # Check each element
        if mn <= e < mx:
            count += 1

    return count


def main():
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # Test a case where some elements are within the range
    print("Counting the elements in [1..10] that are between 5 and 7...")
    print("Result: %d Expected: 2" % count_range(data, 5, 7))

    # Test a case where some elements are within the range
    print("Counting the elements in [1..10] that are between -5 and 77...")
    print("Result: %d Expected: 10" % count_range(data, -5, 77))

    # Test a case where some elements are within the range
    print("Counting the elements in [1..10] that are between 12 and 17...")
    print("Result: %d Expected: 0" % count_range(data, 12, 17))

    # Test a case where the list is empty
    print("Counting the elements in [1..10] that are between 0 and 100...")
    print("Result: %d Expected: 0" % count_range([], 0, 100))

    # Test a case with duplicate values
    data = [1, 2, 3, 4, 1, 2, 3, 4]
    print("Counting the elements in [1, 2, 3, 4, 1, 2, 3, 4] that are",
          "between 2 and 4...")
    print("Result: %d Expected: 4" % count_range(data, 2, 4))

if __name__ == '__main__':
    main()
