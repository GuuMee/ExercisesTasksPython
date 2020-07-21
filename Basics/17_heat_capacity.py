"""
The amount of energy required to increase the temperature of one gram of a material
by one degree Celsius is the material’s specific heat capacity, C. The total amount
of energy required to raise m grams of a material by ΔT degrees Celsius can be
computed using the formula: q = mCΔT.

Write a program that reads the mass of some water and the temperature change
from the user. Your program should display the total amount of energy that must be
added or removed to achieve the desired temperature change.
Hint: The specific heat capacity of water is 4.186 J/g◦C. Because water has a density of 1.0 gram per millilitre,
you can use grams and millilitres interchangeably.

Extend your program so that it also computes the cost of heating the water. Elec�tricity is normally billed using units of kilowatt hours rather than Joules. In this
exercise, you should assume that electricity costs 8.9 cents per kilowatt-hour. Use
your program to compute the cost of boiling water for a cup of coffee.
Hint: You will need to look up the factor for converting between Joules and
kilowatt hours to complete the last part of this exercise.

"""

# my solution


def heat_capacity():
    J_TO_KWH = 2.777e-7
    HEAT_CAPACITY = 4.186
    mass_of_water = int(input("Write some mass of water: "))
    temperature = int(input("Write the temperature change: "))
    energy = mass_of_water * HEAT_CAPACITY * temperature
    electricity = 8.9
    kwh = energy * J_TO_KWH
    cost = electricity * kwh
    print("Energy amount: %.2f" % energy)
    print("cost of cup of coffee: %.2f" % cost)


# Compute the amount of energy needed to heat a volume of water, and the cost of doing so

# Define constraints for the specific heat capacity of water and the price of electricity
WATER_HEAT_CAPACITY = 4.186
ELECTRICITY_PRICE = 8.9
J_TO_KWH = 2.777e-7

# Read the volume from the user
volume = float(input("Enter the amount of water in milliliters: "))
d_temp = float(input("Enter the temperature increase (degrees Celsius): "))

# Compute the energy in Joules
q = volume * d_temp * WATER_HEAT_CAPACITY

# Display the result in Joules
print("That will require %d Joules of energy." % q)

# Compute the cost
kwh = q * J_TO_KWH
cost = kwh * ELECTRICITY_PRICE

# Display the cost
print("That much energy will cost %.2f cents." % cost)
