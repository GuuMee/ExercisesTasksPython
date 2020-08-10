"""
Write a function that determines whether or not a list of values is in sorted order
(either ascending or descending). The function should return True if the list is
already sorted. Otherwise it should return False. Write a main program that reads
a list of numbers from the user and then uses your function to report whether or not
the list is sorted.
Make sure you consider these questions when completing this exercise:
- Is a list that is empty in sorted order?
- What about a list containing one element?
"""


def is_sorted(list):
    sorted_l = 0
    sorted_l = list[0]
    if list == sorted(list):
        return True
    return False


def main():
    list = []
    line = input("Enter the numbers to add the list (in the sorted order or not, blank for quit):")
    while line != "":
        num = float(line)
        list.append(num)
        line = input("Enter the numbers to add the list (in the sorted order or not, blank for quit):")
    sortness = is_sorted(list)
    if sortness:
        print("The list is sorted")
    else:
        print("The list is not sorted")


if __name__ == '__main__':
    main()