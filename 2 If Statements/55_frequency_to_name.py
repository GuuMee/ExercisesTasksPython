"""
Electromagnetic radiation can be classified into one of 7 categories according to its
frequency, as shown in the table below:

Name                Frequency range (Hz)
Radio waves         Less than 3 × 10^9
Microwaves          3 × 10^9 to less than 3 × 10^12
Infrared light      3 × 10^12 to less than 4.3 × 10^14
Visible light       4.3 × 10^14 to less than 7.5 × 10^14
Ultraviolet light   7.5 × 10^14 to less than 3 × 10^17
X-rays              3 × 10^17 to less than 3 × 10^19
Gamma rays          3 × 10^19 or more

Write a program that reads the frequency of the radiation from the user and displays
the appropriate name.

"""

frequency = float(input("Enter the frequency of the radiation:"))

if frequency < (3* 10**9):
    name = "Radio wave"
elif (3 * 10**9) <= frequency < (3 * 10**12):
    name = "Microwave"
elif (3 * 10**12) <= frequency < (4.3 * 10**14):
    name = "Infrared light"
elif (4.3 * 10**14) <= frequency < (7.5 * 10**14):
    name = "Visible light"
elif (7.5 * 10**14) <= frequency < (3 * 10**17):
    name = "Ultraviolet light"
elif (3 * 10**17) <= frequency < (3 * 10**19):
    name = "X-rays"
elif frequency > (3 * 10**19):
    name = "Gamma rays"

print(" Electromagnetic radiation is %s" % name)

