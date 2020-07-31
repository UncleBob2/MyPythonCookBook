from time import time


def error_counting(prompt):
    '''calculate the accuracy of input prompt'''
    global inwords

    words = prompt.split()
    error = 0

    for i in range(len(inwords)):
        if i in (0, len(inwords)-1):
            if inwords[i] == words[i]:
                continue
            else:
                errors += 1
        else:
            if inwords[i] == words[i]:
                if (inwords[i+1] == words[i+1]) and (inwords[i-1] == words[i-1]):
                    continue
                else:
                    errors += 1
            else:
                errors += 1
        return errors

# calculate the typing speed: words per minute


def speed(inprompt, start_time, end_time):
    global time
    global inwords

    inwords = inprompt.split()
    twords = len(inwords)
    speed = twords / time
    return speed

# calculate the total elapsed time


def elapsetime(start_time, end_time):
    time = end_time - start_time
    return time


if __name__ == '__main__':
    prompt = '''So she was considering in her own mind(as well as she the hot day made her feel very sleepy and stupid), 
whether the pleasure of making a daisy-chain would be worth the trouble of getting up and picking the daisies, when suddenly a White
Rabbit with pink eyes ran close by her.'''

print("Type this: ", prompt, " ")
input("Press Enter to begin")

start_time = time()
inprompt = input()
end_time = time()

# collect all the information returned by the function
time = round(elapsetime(start_time, end_time), 2)  # round off the time
speed = speed(inprompt, start_time, end_time)
errors = error_counting(prompt)

# print results
print('###############################')
print("Total time elapsed: ", time, "seconds")
print("Your average typing speed was ", speed, "words per minute")
print("with the total of ", errors, "errors")
print('###############################')
