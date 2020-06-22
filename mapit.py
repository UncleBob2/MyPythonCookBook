#!
import webbrowser, sys, pyperclip


sys.argv


print(sys.argv)

if len(sys.argv) >1:
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()
    print(address)
 
#    https://www.google.com/maps/place/
webbrowser.open('https://www.google.com/maps/place/' + address)
