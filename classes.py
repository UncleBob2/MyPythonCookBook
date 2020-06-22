# Classes uses to make objects: contains fields, methods, instances (objects)
# Fields – data attached to an object
# Init is same as constructor

from datetime import date
import datetime

class User: # user1 is an object/instance of User Class a
    '''A member of FriendFace. For now we are only storing their name and birthday"""
'''
    def __init__(self, full_name, birthday):
        self.name = full_name
        self.birthday = birthday #yyyymmdd

        #Extract first and last name
        name_pieces = full_name.split(" ")
        self.first_name = name_pieces[0]
        self.last_name = name_pieces[-1]

    def age(self):
        """Return the age of the user in years."""
        today = (date.today())
        yyyy = int(self.birthday[0:4])
        mm = int(self.birthday[4:6])
        dd = int(self.birthday[6:8])
        dob = datetime.date(yyyy,mm,dd) #Date of birth
        age_in_days = (today - dob).days
        age_in_years = age_in_days/365
        return int(age_in_years)

user1 = User("Dave Bowman", "19710315")
user2 = User('Arthur Clarke', "20001212")
print(user1.first_name, user1.last_name, user1.age())
print(user2.first_name, user2.last_name, user2.age())

