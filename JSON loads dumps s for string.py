'''Javascript Object Notation
JSON        Python
Object      dictionary
Array       list
String      str
number(int) int
true        True
false       False
null        None

'''

import json


# python string with valid json format with people as objects
people_string = '''
{
    "people": [
    {
    "name": "John Smith",
    "phone": "642-234-3436",
    "emails": ["johnsmith@gosul.com", "john.smith@wprk-di.com"],
    "has_license": false
    },
    {
    "name": "Jane Doe",
    "phone": "454-454-6866",
    "emails": null,
    "has_license": true
    }
    ]
}
'''

# loading a json string into python's object
data = json.loads(people_string)

print(data)
# objects is converted to dictionary
print('Objects is converted to dictionary', type(data))
print()

print(data['people'])
# array of people is converted to list
# since it is a list, we can loop through it
print('Array of people is converted to list', type(data['people']))
print()

for person in data['people']:
    print(type(person))
    print(person)

print()
for person in data['people']:
    print(type(person['name']))
    print(person['name'])

print()
# going reverse - dumping  python's object into JSON string
# want to remove the phone number of each person in the list

for person in data['people']:
    del person['phone']  # the key is phone

new_string = json.dumps(data, indent=2)  # to make data easier to read, use indent
print(new_string)
