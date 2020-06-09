import time
from datetime import datetime


def add_employee(emp, emp_list=None):  # emp_list is evaluated only once at creation
    if emp_list is None:
        emp_list = []
    emp_list.append(emp)
    print(emp_list)


emps = ['John', 'Jane']

add_employee('Corey', emps)
add_employee('John')
add_employee('Jane')


#----------------------------
# this is executed only once; hence, you get the same timenow 3x
def display_time(time=datetime.now()):
    print(time.strftime('%B %d, %Y %H:%M:%S'))


display_time()
time.sleep(1)
display_time()
time.sleep(1)
display_time()


def display_time1(time=None):  # this is correct by defining inside of the function
    if time is None:
        time = datetime.now()
    print(time.strftime('%B %d, %Y %H:%M:%S'))


display_time1()
time.sleep(1)
display_time1()
time.sleep(1)
display_time1()
