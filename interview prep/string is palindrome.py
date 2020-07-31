# Check if string is a palindrome
#https://www.youtube.com/watch?v=y3S0iYFedCw&list=PL5tcWHG-UPH1D-JVSiZI_8I8LPUJtoHdg&index=3

aList = [
    "bear",
    "unique",
    "aga",
    "radar",
    "rotor",
]

for i in range(len(aList)):
    if aList[i] == aList[i][::-1]:
        print("This is a palindrome word: ", aList[i])
