import subprocess
subprocess.call("reset")
import os

current_path = os.path.dirname(__file__)
filename = os.path.join(current_path, "words.txt")

with open(filename, "r") as f:
    for line in f:
        line = line.lower().rstrip()
        if line == line[::-1]:
            print(line)

