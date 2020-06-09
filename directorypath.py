import sys
import os


def List(dir):
    filenames = os.listdir(dir)
    for filename in filenames:
        path = os.path.join(dir, filename)
        print(path)
        print(os.path.abspath(path))

# Define a main() function that prints a little greeting.


def main():
    #List(sys.argv[1])
    print('abspath:     ', os.path.abspath(__file__))
    dir = os.path.dirname(os.path.abspath(__file__))
    List(dir)
    print('abs dirname: ', os.path.dirname(os.path.abspath(__file__)))


if __name__ == "__main__":
    main()
