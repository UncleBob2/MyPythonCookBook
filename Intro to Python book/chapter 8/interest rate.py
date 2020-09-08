import os
import subprocess
subprocess.run('reset')

init_cap = 1
interest_rate = float(input("Enter interest rate in percentage: "))
year = 0
while init_cap <= 2.0:
    init_cap = round(init_cap + init_cap*interest_rate/100 + 0.005, 3)
    year += 1
    print(init_cap)


print('Number of years to double: ', year)
