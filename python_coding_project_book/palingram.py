import os
import subprocess

subprocess.call('reset')

current_path = os.path.dirname(__file__)
filename = os.path.join(current_path, "word.txt")


with open(filename, 'r') as f:
    for word in f:
        word = word.rstrip().lower()
        word_len = len(word)
        for i in range(1, word_len, 1):
            if (word[:word_len-i][::-1] == ):
                print(word, word[:word_len-i][::-1])
        # if word == word[::-1]:  # reverse palindrome
        #     print('This word is palindrome: ', word)
