import os
from datetime import datetime

#print('print all func/commands of os module',dir(os))

os.chdir('/Users/winsorhoang/dev')
print('get current working director getcwd -> ', os.getcwd())

# os.mkdir vs os.makedirs (create sub directory)
try:
    os.makedirs('OS_demo_2/sub_dir')
except FileExistsError:
    print('contents already exist'.upper())

print('list all contents in current directory', os.listdir())

try:
    os.rename('test.txt', 'demo.txt')
except FileNotFoundError:
    print('file does not exist to rename'.upper())

try:
    os.removedirs('OS_demo_2/sub_dir')
except FileNotFoundError:
    print('No existing directory'.upper())

print(os.listdir())

mod_time = os.stat('demo.txt').st_mtime
print('Print the modification time of the file',
      datetime.fromtimestamp(mod_time))


for dirpath, dirnames, filename in os.walk(os.getcwd()):
    print('Current Path:', dirpath)
    print('directories:', dirnames)
    print('Files:', filename)
    print()


try:
    print("HOME:", os.environ['MY_HOME'])
except KeyError:
    print("Environment variable does not exist")

file_path = os.path.join(os.environ.get('HOME'), 'test.txt')
print(file_path)

import sys
print(sys.version)
