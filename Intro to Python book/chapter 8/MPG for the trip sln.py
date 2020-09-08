# Ask user to enter the initial reading of odometer
odometer_last_reading = int(input("Input the reading of the odometer: "))
# Initiate the final sum as 0

finalSum = 0
legs = 0
# Use while loop to ask the user for odometer reading and gas consumed at each leg
while True:
    inp = str(input(
        'Enter both the odometer reading andgas_Value Consumed (separated by comma) :'))
    if inp.strip('') == '':
        break

    input_fields = inp.split(",")
    odometer = eval(input_fields[0])
    gas_Value = eval(input_fields[1])

    print("The MPG value is :", (odometer - odometer_last_reading)/gas_Value)

    finalSum = finalSum + (odometer - odometer_last_reading)/gas_Value
    legs = legs + 1
    odometer_last_reading = odometer
# Print the miles per gallon for whole trip

print("The Final value is :", finalSum/legs)
