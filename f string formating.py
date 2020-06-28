first_name = 'Corey'
last_name = 'Schafer'

sentence = f'My name is {first_name.upper()} {last_name.upper()}'
print(sentence)


person = {'name': 'Jenn', 'age': 23}

# Must use double quote to avoid ening f string early with signal quote
sentence = f"My name is {person['name']} and I am {person['age']}"
print(sentence)

calculation = f'4 times 11 is equal to {4*11}'
print(calculation)


for n in range(1, 11):
    sentence = f'The value is {n:02}'
    print(sentence)

pi = 3.14159265
# floating point format to 4 decimal place
sentence = f'Pi is equal to {pi:.4f}'
print(sentence)

from datetime import datetime

birthday = datetime(1990, 1, 1)
sentence = f'Jenn has a birthday on {birthday:%B %d, %Y}'
print(sentence)
