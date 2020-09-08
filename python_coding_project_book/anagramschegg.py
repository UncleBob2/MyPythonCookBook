# global variables
words = []
file_name = "/Users/winsorhoang/dev/python/python_coding_project_book/words.txt"

# function returns list of anagrams


def anagrams(word):
    if len(word) <= 1:
        yield word
    else:
        for perm in anagrams(word[1:]):
            for i in range(len(word)):
                yield perm[:i] + word[0:1] + perm[i:]


# reads english words from the file and stores in global variable
def get_english_words():
    global words, file_name
    if len(words) > 0:
        return
    f = open(file_name)
    data = f.read()
    f.close()
    words = data.split("\n")


# removes duplicates from given array
def remove_duplicates(data):
    temp = []
    for w in data:
        if w not in temp:
            temp.append(w)
    return temp


# program execution starts from here
if __name__ == "__main__":
    # reading english words and storing in memory
    get_english_words()

    while True:
        print("--------------------------------------------------")
        # taking input from user
        input_str = input("Please enter string (q for quit) : ")
        if input_str == "q":
            break
        # finding anagrams
        temp = list(anagrams(input_str))
        # removing duplicate combinations
        temp = remove_duplicates(temp)
        # filtering based on dictionary words
        temp = [t for t in temp if t in words]
        print(temp)
    print("--------------------------------------------------")
