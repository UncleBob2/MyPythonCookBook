"""Wordcount exercise
1. For the --count flag, implement a print_words(filename) function that counts
how often each word appears in the text and prints:
word1 count1
word2 count2
...

2. For the --topcount flag, implement a print_top(filename) which is similar
to print_words() but which prints just the top 20 most common words sorted
so the most common word is first, then the next most common, and so on.
"""


def print_words(filename):
    f = open(filename, 'r')
    frequency = {}
    newfrequency = {}
    count = 0

    for line in f:  # reading line by line
        txt = line.lower().split()
        print(txt)
# to do, assign each word to the dictionary
    # if the word already in a dictionary increase the count
        for word in txt:
            if word in frequency:
                frequency[word] += 1
            else:
                frequency[word] = 1

    for key, value in sorted(frequency.items(), key=lambda item: item[1], reverse=True):
        print("%s: %s" % (key, value))
    print('\n')
    return


def top_counts(filename):
    f = open(filename, 'r')
    frequency = {}
    newfrequency = {}
    count = 0

    for line in f:  # reading line by line
        txt = line.lower().split()
# to do, assign each word to the dictionary
    # if the word already in a dictionary increase the count
        for word in txt:
            if word in frequency:
                frequency[word] += 1
            else:
                frequency[word] = 1

    for key, value in sorted(frequency.items(), key=lambda item: item[1], reverse=True):
        print("%s: %s" % (key, value))
        count += 1
        if count >= 20:
            break
    print('\n')
    return


# print_words('small.txt')
top_counts('alice.txt')
