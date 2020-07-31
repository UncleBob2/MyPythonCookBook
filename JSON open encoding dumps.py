# JSON is similar to python dictionary, it is shorter than xml (large end tag), quick parse by browers,  uses java syntax
import json

json_file = open('JSON ex1.txt','r',encoding='utf-8')  # see file as dictionary {}
movie = json.load(json_file)
json_file.close()
print(movie)   # converted true, false, null => True, False, None


print('Title: ', movie['title'] )

print(json.dumps(movie))

print(json.dumps(movie, ensure_ascii=False))
