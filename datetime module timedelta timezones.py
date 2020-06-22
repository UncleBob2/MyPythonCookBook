import datetime
import pytz

# naive datetime vs aware

assigned_d = datetime.date(2012, 12, 12)
today = datetime.date.today()
print('Assigned date = {}, Today Date = {},'.format(assigned_d, today))
print('Year = {}, Month = {}, day =  {}'.format(
    today.year, today.month, today.day))

# Monday 0  and Sunday 6 date.weekday()
# Monday 1 ... Saturday = 6 and Sunday 7 isoweekday()

print('today is = {}'.format(today.isoweekday()))


tdelta = datetime.timedelta(days=7)
print('Print the seven days from now', today + tdelta)

# date2 = date1 + timedelta
# timedelta = date1 + date2

bday = datetime.date(2020, 9, 24)
till_bday = bday - today
print('days until celebration', till_bday.days)
print('seconds until celebration = {:,}'.format(till_bday.total_seconds()))

dt = datetime.time(12, 30, 34, 100)
print(dt)

dt = datetime.datetime(2016, 5, 23, 12, 30, 34, 100)
print(dt)

dt = datetime.datetime(2016, 5, 23, 12, 30, 34, tzinfo=pytz.UTC)
print('Timezone aware with pytz = ', dt)

# this is best since less typing
dt_utcnow = datetime.datetime.now(tz=pytz.UTC)
print('Timezone now with pytz = ', dt_utcnow)

dt_mtn = dt_utcnow.astimezone(pytz.timezone('US/Mountain'))
print('Timezone Denver pytz = ', dt_mtn)

dt_mtn = datetime.datetime.now()  # naive time
mtn_tzone = pytz.timezone('US/Mountain')

dt_mtn = mtn_tzone.localize(dt_mtn)  # using localize, it is now time aware
print(dt_mtn)
#strftime - datetime to string
#strptime - string to datetime

# this is string, we need to convert to datetime to manipulate it
dt_str = 'July 26, 2015'
dt = datetime.datetime.strptime(dt_str, "%B %d, %Y")
print(dt)
