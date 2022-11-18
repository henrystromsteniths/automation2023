# This is assignment project 1, a Python script.
# This script is a cost of fuel calculator.
# It calculates the cost for the use of petrol or diesel for travel a certain distance.
# We assume that the consumption of fuel is one litre per ten Kilometres.

# Defaults
distance = 0.0
cost_of_petrol = 0.0
cost_of_diesel = 0.0

distance = float(input ("How far do you plan to travel in Kilometres? "))
fuel_type = str(input("Will you fill up (P)etrol or (D)iesel? "))

if fuel_type == "P":
    cost_of_petrol = float(input("How much does one litre of petrol cost? "))
    print("You will need to spend " + str(distance / 10 * cost_of_petrol) + " for fuel.")

elif fuel_type == "D":
    cost_of_diesel = float(input("How much does one litre of diesel cost? "))
    print("You will need to spend " + str(distance / 10 * cost_of_diesel) + " for fuel.")

else:
    print("Please answer using either the P or D characters.")


# if kgs_or_lbs == "K":
#     din_vikt = (your_weight * 2.22)
#     print("Din vikt är " + str(din_vikt) + " Pounds")
# elif kgs_or_lbs == "P":
#     din_vikt = (your_weight / 2.22)
#     print("Din vikt är " + str(din_vikt) + " Kilogram")
# else:
#     print("Vänligen ange enhet med antingen K eller P.")


# print (your_weight)
# print (kgs_or_lbs)
# print (din_vikt)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


