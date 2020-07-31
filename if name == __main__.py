def main():
    print("First Module's Name: {}".format(__name__))


if __name__ == '__main__':  # is this program running directly from python or being import
    main()
    print('Run directly')
else:
    print('Run from import')
