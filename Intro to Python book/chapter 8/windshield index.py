import subprocess
subprocess.run('reset')


for Temp in range(-20, 50+10, 10):
    if Temp == -20:
        print('\t', Temp, end='\t')
    elif Temp == 50:
        print(Temp)
    else:
        print(Temp, end='\t')


for Vel in range(0, 50+5, 5):
    print(Vel, end='\t')
    for Temp in range(-20, 50+10, 10):
        windchill = 35.74 + 0.6215*Temp - 35.75 * \
            (Vel**0.16) + 0.4275*Temp*(Vel**0.16)
        print("{:.2f}".format(windchill), end="\t")
    print()
