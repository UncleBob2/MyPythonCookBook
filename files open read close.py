# Text files: plain text, xml, json, source code
# Binary files: compiled data, app data, media files: image, audio, video

# # reading files
# with open('exception example.log') as fileobj:
#     bio = fileobj.read()   #no file close is required
# print(bio)

# #Try & Except
# try:
#    with open('future_lottery_numbers.txt') as f:
#        text = f.read()
# except FileNotFoundError:
#       text = 'no file'

# writing file
oceans = ['Pacific','Atlantic', 'Indian', 'Southern', 'Artic']
with open('oceans.txt','w') as f: #create new file if none exist
    for ocean in oceans:
        print(ocean, file=f) # alternatively can use f.write(ocean)

with open('oceans.txt', 'a') as f: # append and not overwrite
    print(23*'=', file=f)
    print('These are the 5 oceans.', file=f)


