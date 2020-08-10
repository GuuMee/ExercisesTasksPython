"""
In a particular jurisdiction, taxi fares consist of a base fare of $4.00, plus $0.25
for every 140 meters traveled. Write a function that takes the distance traveled (in
kilometers) as its only parameter and returns the total fare as its only result. Write a
main program that demonstrates the function.

Hint: Taxi fares change over time. Use constants to represent the base fare and
the variable portion of the fare so that the program can be updated easily when
the rates increase.
"""

BASE_FARE = 4.00
ADDITIONAL_FARE = 0.25
DISTANCE_LIMIT = 140
IN_METERS = 1000


def taxi_fare(distance):
    distance *= IN_METERS
    distance = int(distance)
    fare = 0
    if distance < DISTANCE_LIMIT:
        print("Your taxi fare id $%.2f for the traveled distance" % BASE_FARE)
    else:
        fare += BASE_FARE
        while distance >= DISTANCE_LIMIT:
            distance -= DISTANCE_LIMIT
            fare += ADDITIONAL_FARE

    return print("Your taxi fare for traveled distance is $%.2f" % fare)


travelled_distance = float(input("Enter traveled distance (in kilometers): "))
taxi_fare(travelled_distance)
