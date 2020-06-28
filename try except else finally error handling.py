try:
    f = open('sm0all.txt')
    #var = badvar
    # if f.name == 'corrupt_file.txt':
    #     raise Exception

except FileNotFoundError as e:
    print(e)
except Exception as g:
    print(g)
else:
    print(f.read())
    f.close()
finally:
    print('Excecuting final step ... close database or resources after this code block')
