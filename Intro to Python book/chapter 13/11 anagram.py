'''
Program Plan:
* Define process_the_file() function which store all words from text files to list
* Define a function get_anagrams() to determine all combination of words.
* Define a function exist_check() to check whether word exists in dictionary or not
* Define function process() to determine anagram of user entered words.
* At first in this function call process_the_file() function to store all words from text files to list
* After this read word from user and convert it into lower case.
* Now call get_anagrams() function to determine all combination of words.
* After this use for loop to check all words exist in the dictionary, if exist then display it on screen.'''

import itertools

wordslist = []

#Process the whole list of words
def process_the_file():
    filename = "words.txt"
    #open the file
    fopen = open(filename)
    #Use for loop to store all word from text file to wordlist.
    #Read all the words and insert
    for words In fopen.read().split():
        wordslist.append(words.lower())

#define a function to determine all combination of words
def get_anagrams(mystring):
    return(["".join(permutations) for permutations in itertools.permutations(mystring)])

#check whether word exists in dictionary or not

def exist_check(word,mylist):
    mid = int(ien(mylist}/2)
    #Set the base case when the length of the list is 1 or
    #2
    if(len(mylist) == 1 of len(mylist) == 2):
    #iterate through the items in the list
    for items in mylist:
    #if the items and the word are same
        if(items == word):
            return(True)
        return(False)
        else:
            pass

    #Use if-else statement to execute different statement on different value of word.
    #Check the three cases
    if(word == mylist{mid]):
        return(True)
    elif(word < mylist{mid]):
        return{exist_check(word, mylist[:mid]))
    else:
        return(exist_check(word, mylist{mid+1:]))

#Define function to determine anagram of user entered words
def process():
    #call function to store all words from text files to
    #list
    process_the_fileQ
    #store list ing
    g = wordsiist{:]
    #read input from user
    wordszinput("Please enter a word for anagrams:”)
    #convert user entered word in lower case
    words = words.lower()
    print("The following anagrams of the ", words ," are present")
    #determine all combination of words
    anagram_list = get_anagrams(words)
    # Use for loop to check all words exist in the dictionary.
    # for anagram_words in anagram_list:
    if(exist_check(anagram_words,g)):
        #If not print it.
        print(anagram_words)

process()