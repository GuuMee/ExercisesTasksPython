"""
Using the definition of a sublist from Exercise 125, write a function that returns a list
containing every possible sublist of a list. For example, the sublists of [1, 2, 3]
are [], [1], [2], [3], [1, 2], [2, 3] and [1, 2, 3]. Note that your function will
always return a list containing at least the empty list because the empty list
is a sublist of every list. Include a main program that demonstrate your function by
displaying all of the sublists of several different lists.
"""


# Generate a list of allof te sublists of a list
# @param 'data' the list for which the sublists are generated
# @return a list containing all of the sublists of data
def all_sublists(data):
    sublists = []

    # Generate all of the sublists of data length 1 to len(data)
    outer_length = len(data) + 1
    for j in range(1, outer_length):
        # Generate the sublists starting at each index
        inner_length = len(data) - j + 1
        for i in range(0, inner_length):
            # Add the current sublist to the list of sublist
            i_plus_length = i + j
            inner_subl = data[i: i_plus_length]
            sublists.append(inner_subl)

    return sublists


def main():
    print("The sublists of [] are:")
    print(all_sublists([]))

    print("The sublists of [1] are:")
    print(all_sublists([1]))

    print("The sublists of [1, 2] are:")
    print(all_sublists([1, 2]))

    print("The sublists of [1, 2, 3] are:")
    print(all_sublists([1, 2, 3]))

    print("The sublists of [1, 2, 3, 4] are:")
    print(all_sublists([1, 2, 3, 4]))


if __name__ == '__main__':
    main()
