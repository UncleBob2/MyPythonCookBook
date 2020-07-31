import sys
import os


current_path = os.path.dirname(__file__)
filename = os.path.join(current_path, "words.txt")

# with open(filename, "r") as f:
#     for line in f:
#         print(line)


def List(dir):
    filenames = os.listdir(dir)
    for filename in filenames:
        path = os.path.join(dir, filename)
        print(path)
        print(os.path.abspath(path))


# Define a main() function that prints a little greeting.


def main():
    # List(sys.argv[1])
    print("abspath:     ", os.path.abspath(__file__))
    dir = os.path.dirname(os.path.abspath(__file__))
    List(dir)
    print("abs dirname: ", os.path.dirname(os.path.abspath(__file__)))


if __name__ == "__main__":
    main()
