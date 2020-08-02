"""
Write a program that converts a binary (base 2) number to decimal (base 10). Your
program should begin by reading the binary number from the user as a string. Then
it should compute the equivalent decimal number by processing each digit in the
binary number. Finally, your program should display the equivalent decimal number
with an appropriate message.

"""
i = 0
decimal = 0
bits = input("Enter the binary number to convert to decimal: ")
length = (len(bits))

while i < length:
    bit = int(bits[i])
    two_th = 2 ** i
    decimal += (bit * two_th)
    i += 1

print("Decimal number is %d" % decimal)

