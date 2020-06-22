student = {'name': 'John', 2343: 'student ID', 'age':25, 'courses': ['Math', 'CompSci']}

print('Dictionary key "name": value = ', student['name'])
print('Dictionary key "courses": value = ', student['courses'])
print('Dictionary key "2343": value = ', student[2343])


# to avoid error when key does not exist.
print('Using get to fetch key "name": value = ', student.get('name'))
print('Using get to fetch key "telephone": value = ', student.get('phone', 'Not Found'))
#define telephone key
student['phone'] = '555-5555'
print('Using get to fetch key "phone": value = ', student.get('phone', 'Not Found'))

student.update({'name': 'Jane', 'age': 26, 'phone': '454-4545'})
print(student)

del student['age']

student_id = student.pop(2343)

print('delete student age using del and pop the student_id = ', student)
print(student_id)

for key,value in student.items():
    print(key,value)
