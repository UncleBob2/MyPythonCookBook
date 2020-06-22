# file objects
# context manager - no close file required, import line by line to avoid memory issues
with open('small.txt', 'r') as f:
    for line in f:
        print(line, end='')

# to specify the number of char to read use below

with open('small.txt', 'r') as f:
    size_to_read = 10
    f_contents = f.read(size_to_read)

    while len(f_contents) > 0:
        print(f_contents, end='*')
        f_contents = f.read(size_to_read)

# f.tell() or f.seek()

# # copy file line by line
# with open('small.txt', 'r') as readfile:
#     with open('small_copy.txt', 'w') as writefile:
#         for line in readfile:
#             writefile.write(line)

# # copy binary file line by line i.e. jpg
# with open('small.txt', 'rb') as readfile:
#     with open('small_copy.txt', 'wb') as writefile:
#         for line in readfile:
#             writefile.write(line)

# copy binary file line by line i.e. jpg
with open('alice.txt', 'rb') as rf:
    with open('alice_copy.txt', 'wb') as wf:
        chunk_size = 4096
        rf_chunk = rf.read(chunk_size)
        while len(rf_chunk) >0:
            wf.write(rf_chunk)
            rf_chunk = rf.read(chunk_size)


