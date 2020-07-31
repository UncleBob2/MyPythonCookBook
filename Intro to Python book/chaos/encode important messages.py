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

