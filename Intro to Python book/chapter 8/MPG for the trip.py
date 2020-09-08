import subprocess
subprocess.run('reset')

leg_entry = []
x = ()
mile = []
gas = []
mpg = 0
gas_used = 0


start = int(input('Please enter the odometer: '))
leg_entry.append(str(start) + ' ' + '0')

print(leg_entry)
while x != (""):
    x = input(
        'Please input current odometer reading an amount of gas used i.e. xxxxx("mile") xxx("gallon"): ')
    leg_entry.append(x)

leg_entry.pop(-1)
print(leg_entry)

a = leg_entry

for index in range(len(a)):
    temp = a[index].split(" ")
    mile.append(int(temp[0]))
    gas.append(int(temp[1]))

for i in range(1, len(a)):
    print('leg', i, ((mile[i]-mile[i-1])/gas[i]))
    mpg = mpg + (mile[i]-mile[i-1])
    gas_used = gas_used + gas[i]

total = mpg/gas_used
print("Total MPG", total)
