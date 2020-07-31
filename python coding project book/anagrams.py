import os
import subprocess

subprocess.run('reset')

cwd = os.path.dirname(__file__)
filename = os.path.join(cwd, 'words.txt')

user_ip = input("Enter a word for anagrams: ")
user_word = user_ip.lower()
srt_user_ip = sorted(list(user_ip))

with open(filename, 'r') as f:
    for word in f:
        word = word.rstrip().lower()
        srt_word = sorted(list(word))
        if srt_word == srt_user_ip:
            print(user_word, word)
