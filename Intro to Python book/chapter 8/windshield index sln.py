import subprocess
subprocess.run('reset')


def compute(speed, temp):
    return(35.74+(0.6215*temp)-(35.75*(speed**0.16)) +
           (0.4275 * temp*(speed**0.16)))


def show_table():
    windSpeed = [speed for speed in range(-5, 55, 5)]
    temp = [temperature for temperature in range(- 30, 70, 10)]

    for speedItems in windSpeed:
        for tempItems in temp:
            # *if condition for checking the range
            if(speedItems == -5 and tempItems == -30):
                print(" \t", end="")
            elif(speedItems == -5):
                print(tempItems, end="\t")
            elif(tempItems == -30):
                print(speedItems, end='\t')
            else:
                print(round(compute(speedItems, tempItems), 2), end="\t")
        print("\n")
    print(windSpeed)
    print(temp)


show_table()
