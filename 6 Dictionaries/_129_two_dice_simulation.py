"""
In this exercise you will simulate 1,000 rolls of two dice. Begin by writing a func�tion that simulates rolling a pair of six-sided dice. Your function will not take any
parameters. It will return the total that was rolled on two dice as its only result.
Write a main program that uses your function to simulate rolling two six-sided
dice 1,000 times. As your program runs, it should count the number of times that each
total occurs. Then it should display a table that summarizes this data. Express the
frequency for each total as a percentage of the total number of rolls. Your program
should also display the percentage expected by probability theory for each total.
Sample output is shown below.
"""


from random import randrange

NUM_RUNS = 1000
D_MAX = 6

def two_dice():
    d1 = randrange(1, D_MAX + 1)
    d2 = randrange(1, D_MAX + 1)

    return d1 + d2


def main():
    expected = {2: 1/36, 3: 2/36, 4: 3/36, 5: 4/36,
                6: 5/36, 7: 6/36, 8: 5/36, 9: 4/36,
                10: 3/36, 11: 2/36, 12: 1/36}

    counts = {2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0,
              8: 0, 9: 0, 10: 0, 11: 0, 12: 0}

    for i in range(NUM_RUNS):
        t = two_dice()
        counts[t] = counts[t] + 1

    print("Total    Simulated   Expected")
    print("           Percent    Percent")
    for i in sorted(counts.keys()):
        print("%5d %11.2f %10.2f" % (i, counts[i] / NUM_RUNS * 100, expected[i] * 100))


if __name__ == '__main__':
    main()
