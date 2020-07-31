import datetime
import pytz
# the goal of __repr__ is to be unambiguous
# the goal of __str__ is to be readable

a = [1, 2, 3, 4]
b = 'sample string'

print(str(a))
print(repr(a))  # is more for developer

print('using str', str(b))
print('using repr', repr(b))

a = datetime.datetime(2020, 7, 11, 5, 55, 34, 454, tzinfo=pytz.UTC)
print('using str', str(a))
print('using repr which we can copy and paste for eval ', repr(a))
