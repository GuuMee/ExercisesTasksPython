"""
The wavelength of visible light ranges from 380 to 750 nanometers (nm). While the
spectrum is continuous, it is often divided into 6 colors as shown below:

Color Wavelength (nm)
Violet 380 to less than 450
Blue 450 to less than 495
Green 495 to less than 570
Yellow 570 to less than 590
Orange 590 to less than 620
Red 620 to 750

Write a program that reads a wavelength from the user and reports its color.
Display an appropriate error message if the wavelength entered by the user
is outside of the visible spectrum.
"""

wave_length = int(input("Enter the wave length: "))

if 380 <= wave_length < 450:
    color = "Violet"
elif 450 <= wave_length < 495:
    color = "Blue"
elif 495 <= wave_length < 570:
    color = "Green"
elif 570 <= wave_length < 590:
    color = "Yellow"
elif 590 <= wave_length < 620:
    color = "Orange"
elif 620 <= wave_length < 750:
    color = "Red"
else:
    color = ''

if color == '':
    print("The entered wavelength is outside of the visible spectrum")
else:
    print("The color by your wave length will be %s " % color)


