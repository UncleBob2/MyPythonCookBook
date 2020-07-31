message1 = input("Please enter the sequence of numbers to decode:  ")
# 104,101,108,108,111,32,119,111,114,100,44,32,105,32,97,109,32,104,101,114,101

message = message1.split(",")
print(message)

for i in range(len(message)):
    message[i] = eval(message[i])

for num in message:
    x = chr(num)
    print(x, end="")


print()


"""
message = ""
for numStr in message1.split(","):
    codeNum = eval(numStr)  # convert digits to a number
    message = message + chr(codeNum)  # concatentate character to message
print("\nThe decoded message is:", message)
"""

