"""
Write a program that reads a sound level in decibels from the user. If the user
enters a decibel level that matches one of the noises in the table then your program
should display a message containing only that noise. If the user enters a number
of decibels between the noises listed then your program should display a message
indicating which noises the level is between. Ensure that your program also generates
reasonable output for a value smaller than the quietest noise in the table, and for a
value larger than the loudest noise in the table.

"""
NOISES = {
    "Jackhammer": 130,
    "Gss lawnmower": 106,
    "Alarm clock": 70,
    "Quiet room": 40
}
JACKHAMMER = 130
GAS_LAWNMOVER = 106
ALARM_CLOCK = 70
QUIET_ROOM = 40

sound_level = int(input("Enter the sound level int decibels: "))

if sound_level == JACKHAMMER:
    print("This is Jackhammer's sound")
elif sound_level == GAS_LAWNMOVER:
    print("This is Gas lawnmower's sound")
elif sound_level == ALARM_CLOCK:
    print("This is Alarm clock's sound")
elif sound_level == QUIET_ROOM:
    print("This is sound of Quiet room")
elif sound_level < QUIET_ROOM:
    print("This sound has the smaller than the quietest noise")
elif sound_level > JACKHAMMER:
    print("This sound has the larger than the loudest noise")
elif QUIET_ROOM < sound_level < ALARM_CLOCK:
    print("The sound noise between the 'Quiet room' and the 'Alarm clock' noise")
elif ALARM_CLOCK < sound_level < GAS_LAWNMOVER:
    print("The sound noise between the 'Alarm clock' and the 'Gas lawnmower' noise")
elif GAS_LAWNMOVER < sound_level < JACKHAMMER:
    print("The sound noise between the 'Gas lawnmower' and the 'Jackhammer' noise")

