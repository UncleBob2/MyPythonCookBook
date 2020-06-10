import datetime
gvr = datetime.date(1956, 1, 31)
message = "GVR was born on {:%A, %B %d, %Y}."
print(message.format(gvr)) #GVR was born on Tuesday, January 31, 1956.


launch_date = datetime.date(2017,3,30)
launch_time = datetime.time(22,27,0)
launch_datetime = datetime.datetime(2017,3,30, 22, 27,0)
print('Rocket launch date" ', launch_date) #2017-03-30
print('Rocket launch time', launch_time) #22:27:00
print(launch_datetime) #2017-03-30 22:27:00

millinium = datetime.date(2000,1,1)
delta = datetime.timedelta(100) #days after
print('100 days after 2000: ' ,millinium + delta)



import time
from datetime import datetime
dateTimeObj = datetime.now()
gvr = datetime.now()

# Access the member variables of datetime object to print date & time information
print('\nDate: ',dateTimeObj.year, '/', dateTimeObj.month, '/', dateTimeObj.day)
print('Time: ', dateTimeObj.hour, ':', dateTimeObj.minute, ':', dateTimeObj.second, '.', dateTimeObj.microsecond)

#converting datetime  object to string
timestampStr = dateTimeObj.strftime("%d-%b-%Y (%H:%M:%S.%f)")
print('String Current Timestamp : ', timestampStr)

# get the date object from datetime object
dateObj = dateTimeObj.date()
print('\nQuick date format', dateObj)

timeObj = dateTimeObj.time()
timeStr = timeObj.strftime("%H:%M:%S.%f")
print('Quick time format', timeObj)








def main():
    print('\n*** Get Current date & timestamp using datetime.now() ***')

    # Returns a datetime object containing the local date and time
    dateTimeObj = datetime.now()

    # Access the member variables of datetime object to print date & time information
    print(dateTimeObj.year, '/', dateTimeObj.month, '/', dateTimeObj.day)
    print(dateTimeObj.hour, ':', dateTimeObj.minute, ':', dateTimeObj.second, '.', dateTimeObj.microsecond)

    print(dateTimeObj)

    # Converting datetime object to string
    timestampStr = dateTimeObj.strftime("%d-%b-%Y (%H:%M:%S.%f)")
    print('Current Timestamp : ', timestampStr)

    timestampStr = dateTimeObj.strftime("%H:%M:%S.%f - %b %d %Y ")
    print('Current Timestamp : ', timestampStr)

    print('*** Fetch the date only from datetime object ***')

    # get the date object from datetime object
    dateObj = dateTimeObj.date()

    # Print the date object
    print(dateObj)

    # Access the member variables of date object to print
    print(dateObj.year, '/', dateObj.month, '/', dateObj.day)

    # Converting date object to string
    dateStr = dateObj.strftime("%b %d %Y ")
    print(dateStr)

    print('*** Fetch the time only from datetime object ***')

    # get the time object from datetime object
    timeObj = dateTimeObj.time()
    # Access the member variables of time object to print time information
    print(timeObj.hour, ':', timeObj.minute, ':', timeObj.second, '.', timeObj.microsecond)

    # It contains the time part of the current timestamp, we can access it's member variables to get the fields or we can directly print the object too
    print(timeObj)

    # Converting date object to string
    timeStr = timeObj.strftime("%H:%M:%S.%f")
    print(timeStr)

    print('*** Get Current Timestamp using time.time() ***')

    # Get the seconds since epoch
    secondsSinceEpoch = time.time()

    print('Seconds since epoch : ', secondsSinceEpoch)

    # Convert seconds since epoch to struct_time
    timeObj = time.localtime(secondsSinceEpoch)

    print(timeObj)

    # get the current timestamp elements from struct_time object i.e.
    print('Current TimeStamp is : %d-%d-%d %d:%d:%d' % (
        timeObj.tm_mday, timeObj.tm_mon, timeObj.tm_year, timeObj.tm_hour, timeObj.tm_min, timeObj.tm_sec))

    # It does not have the microsecond field

    print('*** Get Current Timestamp using time.ctime() *** ')

    timeStr = time.ctime()

    print('Current Timestamp : ', timeStr)


if __name__ == '__main__':
    main()