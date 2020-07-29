"""
In a particular jurisdiction, older license plates consist of three uppercase letters
followed by three numbers. When all of the license plates following that pattern had
been used, the format was changed to four numbers followed by three uppercase
letters.
Write a program that begins by reading a string of characters from the user. Then
your program should display a message indicating whether the characters are valid
for an older style license plate or a newer style license plate. Your program should
display an appropriate message if the string entered by the user is not valid for either
style of license plate.
"""
import re

plate = input("Enter the licence plate: ")

# if len(plate) ==6 and plate[0] >= "A" and plate[0] <= "Z" and \
#     plate[1] >= "A" and plate[1] <= "Z" and \
#     plate[2] >= "A" and plate[2] <= "Z" and \
#     plate[3] >= "0" and plate[4] <= "9" and \
#     plate[4] >= "0" and plate[5] <= "9" and \
#     plate[5] >= "0" and plate[6] <= "9":

# elif len(plate) == 7 and plate[0] >= "0" and plate[0] <= "9" and \
#     plate[1] >= "0" and plate[1] <= "9" and \
#     plate[2] >= "0" and plate[2] <= "9" and \
#     plate[3] >= "0" and plate[3] <= "9" and \
#     plate[4] >= "A" and plate[4] <= "Z" and \
#     plate[5] >= "A" and plate[5] <= "Z" and \
#     plate[6] >= "A" and plate[6] <= "Z":

reg_l = "[a-zA-Z]{3}$"
reg_n3 = "[0-9]{3}"
reg_n4 = "[0-9]{4}"

pattern1 = re.compile(reg_l+reg_n3)
pattern2 = re.compile(reg_n4+reg_l)

if len(plate) == 6 and pattern1:
    print("The plate is a valid older style plate.")
elif len(plate) ==7 and pattern2:
    print("The plate is a valid never style plate.")
else:
    print("The plate is not valid.")



