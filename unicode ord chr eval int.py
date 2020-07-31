message1 = input("Please enter the sequence of numbers to decode:  ")
# 104,101,108,108,111,32,119,111,114,100,44,32,105,32,97,109,32,104,101,114,101

for numStr in message1.split(","):
    codeNum = eval(numStr)  # convert digits to a number
    message = message + chr(codeNum)  # concatentate character to message
print("\nThe decoded message is:", message)


def main():
    print("This program converts a textual message into a sequence")
    print(
        "of numbers representing the Unicode encoding of themessage.\n"
    )  # Get the message to encode
    message = input("Please enter the message to encode: ")

    for char in message:
        x = ord(char)
        print(x, end=",")


main()
