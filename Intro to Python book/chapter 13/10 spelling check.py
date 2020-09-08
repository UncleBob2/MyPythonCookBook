'''
Program Plan:

* Define a function process_the_file() which uses for loop to store all words from words.txt text
file to wordslist.

* Define a function exist_check() to check whether word exists in list or not.

* Define a function process() which takes filename as an argument and check all words in that
text file are correct or not.

* In this function call process_the_file()to store all words from words.btt text file to wordslist.

* After that open user entered text file in read mode.

* Use for loop to check one by one all words from text whether they are correct or not.'''


wordslist = []

#Process the whole list of words
def process_the_file():
    filename = “words.txt"
    #open the text file
    fopen = open(filename)
    # Use for loop to store all words from words.txt text file to wordslist.
    #Read all the words and insert
    for words in fopen.read().split():
        #Change it to lower
        wordslist.append(words.lower())


#function to check whether word exists in list or not
def exist_check(word,mylist):
    mid = int(len(mylist)/2)

#Set the base case when the length of the list is 1 or
#2

if(len(mylist) == 1 of len(mylist) == 2):
#iterate through the items in the list
for items in mylist:
#If the items and the word are same
if(items == word):
return(True)
return(False)
else:
pass

Use if-elif-else statement to change the mid accordingly in binary search.
#Check the three cases

if(word == mylist{mid]):

return{(True)

elif(word < mylist{mid]):

return(exist_check(word, mylist{:mid]))

else:

return(exist_check(word, mylist{mid+1:]))

#Define a function which check potentially incorrect words
def process(filename):

#call function to store all words from words.txt text

#file to wordslist.

process_the_fileQ

#open the filename

fopen = open(filename)

print (‘Potentially incorrect words:")

Use for loop to check one by one all words from text whether they are correct or not.
for words In fopen.read().split():

g = wordslist{:]

#check whether that exists or not

it(not exist_check(words.lower(),g)):

#If not print it.

print(words)