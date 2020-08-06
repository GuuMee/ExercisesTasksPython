"""
What’s the minimum number of times you have to flip a coin before you can have
three consecutive flips that result in the same outcome (either all three are heads or
all three are tails)? What’s the maximum number of flips that might be needed?
How many flips are needed on average? In this exercise we will explore these
questions by creating a program that simulates several series of coin flips.
Create a program that uses Python’s random number generator to simulate flipping
a coin several times. The simulated coin should be fair, meaning that the probability
of heads is equal to the probability of tails. Your program should flip simulated
coins until either 3 consecutive heads of 3 consecutive tails occur. Display an H each
time the outcome is heads, and a T each time the outcome is tails, with all of the
outcomes shown on the same line. Then display the number of flips needed to reach
3 consecutive flips with the same outcome. When your program is run it should
perform the simulation 10 times and report the average number of flips needed.
"""

from random import choice

LIMIT = 3
SIMULATION_NUMBER = 10

s = 0
i = 0
coins = ["T", "H"]
three_H = ["H", "H", "H"]
three_T = ["T", "T", "T"]
total_count = 0

while s <= SIMULATION_NUMBER:
    count = 0
    total = ""
    result = []
    cons3 = False

    while not cons3:
        coin = choice(coins)
        result.append(coin)
        total += coin + " "
        list_length = len(result)
        if list_length >= 3:
                if result[-3:] == three_H or result[-3:] == three_T:
                    cons3 = True
                i += 0

    count = len(result)
    print(total, "(%d flips)" % count,  end="")
    print()
    total_count += count
    s += 1

average = total_count / SIMULATION_NUMBER

print("On average, %.1f flips were neded" % average)
