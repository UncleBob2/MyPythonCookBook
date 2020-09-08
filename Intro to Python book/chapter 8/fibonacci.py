import subprocess
subprocess.run('reset')

listF = [1, 1]
x = int(input('Enter nth Fibonacci number: '))

for i in range(2, x, 1):
    sum = listF[i-2]+listF[i-1]
    listF.append(sum)

print(listF)
print('The nth Fibonacci number is: ', listF[x-1])
