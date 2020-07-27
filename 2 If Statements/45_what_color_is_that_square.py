"""
Positions on a chess board are identified by a letter and a number. The letter identifies
the column, while the number identifies the row.

Write a program that reads a position from the user. Use an if statement to deter�mine if the column begins with a black square or a white square. Then use modular
arithmetic to report the color of the square in that row. For example, if the user enters
a1 then your program should report that the square is black. If the user enters d5
then your program should report that the square is white. Your program may assume
that a valid position will always be entered. It does not need to perform any error
checking.

"""
BLACK_letters1 = ['a', 'c', 'e', 'g']
BLACK_numbers1 = ['1', '3', '5', '7']

BLACK_letters2 = ['b', 'd', 'f', 'h']
BLACK_numbers2 = ['2', '4', '6', '8']

position = input("Enter the position of the chess board from a-h for rows and 1-8 for columns (a1): ")

if position[0] in BLACK_letters1 and position[1] in BLACK_numbers1 \
        or position[0] in BLACK_letters2 and position[1] in BLACK_numbers2:
    print("The position is BLACK")
else:
    print("The position is WHITE!")