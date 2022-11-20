# This is a test script for the test of assignment project 1, a Python script.
# This script tests a cost of fuel calculator.
# The calculator calculates the cost for the use of petrol or diesel for travel a certain distance.
# We assume that the consumption of fuel is one litre per ten Kilometres.
# We compare the calculated result from the script with the expected result.

# Defaults
distance = 0.0
cost_of_petrol = 0.0
cost_of_diesel = 0.0

distance = 100.0 # float(input ("How far do you plan to travel in Kilometres? "))
fuel_type = "P" # str(input("Will you fill up (P)etrol or (D)iesel? "))

if fuel_type == "P":
    cost_of_petrol = 20.0 # float(input("How much does one litre of petrol cost? "))
    print("You will need to spend " + str(distance / 10 * cost_of_petrol) + " for petrol.")
    total_cost_of_petrol = (distance / 10 * cost_of_petrol)

if fuel_type == "D":
    cost_of_diesel = 30.0 # float(input("How much does one litre of diesel cost? "))
    print("You will need to spend " + str(distance / 10 * cost_of_diesel) + " for diesel.")
    total_cost_of_diesel = (distance / 10 * cost_of_diesel)

if (fuel_type != "P") and (fuel_type != "D"):
    print("Please answer using either the P or D characters.")

if fuel_type == "P":
    assert ( (fuel_type in "P") or (fuel_type in "D"))

if fuel_type == "D":
    assert (float(total_cost_of_diesel) == float(300.0))

def calculate_total_cost_of_petrol():
    return (distance / 10 * cost_of_petrol)

def test_answer():
    assert (calculate_total_cost_of_petrol == 200.00)

test_answer()

