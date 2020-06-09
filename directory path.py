import sys
import os


def List(dir):
    filenames = os.listdir(dir)
    for filename in filenames:
        path = os.path.join(dir, filename)
        print(path)
        print(os.path.abspath(path))

# Define a main() function that prints a little greeeting.


def main():
    List(sys.argv[1])


main()
