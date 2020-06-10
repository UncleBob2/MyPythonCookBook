#tuple assignment
a,b,c,d,e,f = 10,20,30,40,50,60
u,v,w,x, y, z = 'python'

print(a,b,c,d,e,f)
print(u,v,w,x,y,z)
print()

a,b,c,d,e,f = u,v,w,x, y, z
u, v, w, x, y, z = z, y, x, w, v, u

print(a,b,c,d,e,f)
print(u,v,w,x,y,z)
print()

person_dictionary = {'name': "Trey", 'company': "Truthful Technology LLC"}
for key, value in person_dictionary.items():
    print(f"Key {key} has value {value}")
print()

# example of typical code
def reformat_date(mdy_date_string):
    """Reformat MM/DD/YYYY string into YYYY-MM-DD string."""
    date = mdy_date_string.split('/')
    return f"{date[2]}-{date[0]}-{date[1]}" # difficult to read

mdy_date_string = '05/12/2011'
print('original format: ', mdy_date_string)
print('formatted date: ', reformat_date(mdy_date_string))

# better multiple assignment for readability
def reformat_date(mdy_date_string):
    """Reformat MM/DD/YYYY string into YYYY-MM-DD string."""
    month, day, year = mdy_date_string.split('/')
    return f"{year}-{month}-{day}"

print()
print('formatted date with better readable code ', reformat_date(mdy_date_string))

