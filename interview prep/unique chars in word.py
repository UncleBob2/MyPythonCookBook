# Technical Interview: Check if string has unique characters
# https://www.youtube.com/watch?v=UqEU-obRUnI&list=PL5tcWHG-UPH1D-JVSiZI_8I8LPUJtoHdg

aList = ["bear", "unique"]


for idex in range(len(aList)):
    if len(aList[idex]) == len(set(aList[idex])):
        print("all unique characters in the word:", aList[idex])

