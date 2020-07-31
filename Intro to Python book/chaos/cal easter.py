import datetime

# strptime is short for "parse time" where strftime is for "formatting time".
input_year = eval(input("Enter a year from 1900 to 2099 to compute Easter:  "))

if input_year < 1900 or input_year > 2099:
    print("Input is not within required year")
else:
    a = input_year % 19
    b = input_year % 4
    c = input_year % 7
    d = (19 * a + 24) % 30
    e = (2 * b + 4 * +6 * d + 5) % 7
    StartDate = "3/22/" + str(input_year)
    date_1 = datetime.datetime.strptime(StartDate, "%m/%d/%Y")
    adj = d + e
    if (
        input_year == 1954
        or input_year == 1981
        or input_year == 2049
        or input_year == 2076
    ):
        adj = adj - 7
    end_date = date_1 + datetime.timedelta(days=(adj))
    print("The date of Easter will be ", end_date.strftime("%m/%d/%Y"))

