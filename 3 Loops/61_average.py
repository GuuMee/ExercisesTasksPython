"""
In this exercise you will create a program that computes the average of a collection
of values entered by the user. The user will enter 0 as a sentinel value to indicate
that no further values will be provided. Your program should display an appropriate
error message if the first value entered by the user is 0.

Hint: Because the 0 marks the end of the input it should not be included in the
average.
"""

items = []
total = 0
i = 0

while 1:
   i += 1
   item = input('Enter item %d: '%i)
   if item == "0":
      break
   items.append(int(item))

total = sum(items)
avg = total/len(items)

print("Collection of the values:", items)
print("Total of the collection:", total)
print("Average of the collection: %.2f" % avg)
