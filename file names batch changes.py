import os


#print('print all func/commands of os module',dir(os))

os.chdir('/Users/winsorhoang/Documents/Planet examples')

filenames = os.listdir()

for filename in filenames:
    # print(filename)
    f_name, f_ext = os.path.splitext(filename)
    # print(f_name.split('#'))
    f_title, f_num = f_name.split('-')
    f_title = f_title.strip()
    f_num = f_num.strip()[1:].zfill(2)
    print('{} {}{}'.format(f_num, f_title, f_ext))
    new_name = '{} {}{}'.format(f_num, f_title, f_ext)
    os.rename(filename, new_name)

# try:
#     os.rename('test.txt', 'demo.txt')
# except FileNotFoundError:
#     print('file does not exist to rename'.upper())

# try:
#     os.removedirs('OS_demo_2/sub_dir')
# except FileNotFoundError:
#     print('No existing directory'.upper())

# print(os.listdir())

# mod_time = os.stat('demo.txt').st_mtime
# print('Print the modification time of the file',
#       datetime.fromtimestamp(mod_time))


# for dirpath, dirnames, filename in os.walk(os.getcwd()):
#     print('Current Path:', dirpath)
#     print('directories:', dirnames)
#     print('Files:', filename)
#     print()
