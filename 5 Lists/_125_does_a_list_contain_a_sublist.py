"""
A sublist is a list that makes up part of a larger list. A sublist may be a list
containing a single element, multiple elements, or even no elements at all. For example,
[1], [2], [3] and [4] are all sublists of [1, 2, 3, 4]. The list [2, 3] is also a
sublist of [1, 2, 3, 4], but [2, 4] is not a sublist [1, 2, 3, 4] because
the elements 2 and 4 are not adjacent in the longer list. The empty list is a sublist of
any list. As a result, [] is a sublist of [1, 2, 3, 4]. A list is a sublist of itself,
meaning that [1, 2, 3, 4] is also a sublist of [1, 2, 3, 4].
In this exercise you will create a function, isSublist, that determines whether
or not one list is a sublist of another. Your function should take two lists, larger
and smaller, as its only parameters. It should return True if and only if smaller
is a sublist of larger. Write a main program that demonstrates your function.
"""


# The function that determines whether or not one list is a sublist of another.
# @param 'larger' longer list
# @param 'smaller' smaller list
# @return True if and only if smaller list is a sublist of larger
def is_sublist(larger, smaller):
    result = False
    len_sm = len(smaller)
    len_lg = len(larger)
    if len_sm <= len_lg:
        x = smaller[1] - smaller[0]
        for i in range(0, len_lg):
            if smaller:
                    if larger[i] - larger[i - 1] == x:
                        result = True
            elif not smaller:
                result = True
    elif len_sm > len_lg:
        result = "The sublist should be smaller or equal to"

    return result


def main():
    larger = list(map(int, input("Enter larger list items followed by space (blank for quit): ").split()))
    smaller = list(map(int, input("Enter smaller list items followed by space (blank for quit): ").split()))
    sublist = is_sublist(larger, smaller)
    if sublist == True:
        print("Your smaller one is Sublist of larger list!")
    else:
        print("Your smaller list isn't sublist")


if __name__ == '__main__':
    main()
