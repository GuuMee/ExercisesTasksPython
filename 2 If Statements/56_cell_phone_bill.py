"""
A particular cell phone plan includes 50 minutes of air time and 50 text messages
for $15.00 a month. Each additional minute of air time costs $0.25, while additional
text messages cost $0.15 each. All cell phone bills include an additional charge of
$0.44 to support 911 call centers, and the entire bill (including the 911 charge) is
subject to 5 percent sales tax.

Write a program that reads the number of minutes and text messages used in a
month from the user. Display the base charge, additional minutes charge (if any),
additional text message charge (if any), the 911 fee, tax and total bill amount. Only
display the additional minute and text message charges if the user incurred costs in
these categories. Ensure that all of the charges are displayed using 2 decimal places.
"""

BASE = 50
BASE_A_MONTH = 15.00
ADDITIONAL_EACH_MINUTE = 0.25
ADDITIONAL_EACH_MESSAGE = 0.15
ADDITIONAL_CHARGE = 0.44
SALES_TAX = 0.05

minutes = int(input("Write the number of minutes: "))
messages = int(input("Enter the number of text messages: "))

if minutes and messages > BASE:
    charge_mess = (messages - BASE) * ADDITIONAL_EACH_MESSAGE
    charge_min = (minutes - BASE) * ADDITIONAL_EACH_MINUTE
    print("The base charge is $%d a month, \
            \nAmount for additional  minutes - $%.2f \
            \nAmount for additional messages $%.2f, \nFee $%.2f for call center \
            \nENTIRE BILL: %.2f"
          % (BASE_A_MONTH, charge_min, charge_mess, ADDITIONAL_CHARGE,
             (BASE_A_MONTH + charge_min + charge_mess + ADDITIONAL_CHARGE)))

elif messages > BASE:
    charge_mess = (messages - BASE) * ADDITIONAL_EACH_MESSAGE
    print("The base charge is $%d a month, \
                \nAmount for additional messages $%.2f, \nFee $%.2f for call center \
                \nENTIRE BILL: %.2f"
          % (BASE_A_MONTH, charge_mess, ADDITIONAL_CHARGE,
             (BASE_A_MONTH + charge_mess + ADDITIONAL_CHARGE)))

elif minutes > BASE:
    charge_min = (minutes - BASE) * ADDITIONAL_EACH_MINUTE
    print("The base charge is $%d a month, \
                \nAmount for additional  minutes - $%.2f, \nFee $%.2f for call center \
                \nENTIRE BILL: %.2f"
          % (BASE_A_MONTH, charge_min, ADDITIONAL_CHARGE,
             (BASE_A_MONTH + charge_min + ADDITIONAL_CHARGE)))
else:
    charge_mess = ''
    charge_min = ''
    print("The base charge is %.2f a month,\
          \n$%.2f fee for call center \
        \n ENTIRE BILL: %.2f" % (BASE_A_MONTH, ADDITIONAL_CHARGE,
          (BASE_A_MONTH+ADDITIONAL_CHARGE)))
