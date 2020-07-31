import requests
import json

r = requests.get('https://xkcd.com/353')

print(r)

# print(dir(r))

'''<Response [200]>
['__attrs__', '__bool__', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__enter__', '__eq__', '__exit__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__nonzero__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setstate__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_content', '_content_consumed', '_next', 'apparent_encoding', 'close', 'connection', 'content', 'cookies', 'elapsed', 'encoding', 'headers', 'history', 'is_permanent_redirect', 'is_redirect', 'iter_content', 'iter_lines', 'json', 'links', 'next', 'ok', 'raise_for_status', 'raw', 'reason', 'request', 'status_code', 'text', 'url']'''

# print(help(r))
# download png file

'''
r = requests.get('https://imgs.xkcd.com/comics/python.png')

with open('comic.png', 'wb') as f:
    f.write(r.content)
# print(r.status_code)
print('is my website ok', r.ok)

# get data
payload = {'page': 2, 'count': 25}
r = requests.get('https://httpbin.org/get', params=payload)
print(r.text)
'''

# post data
payload = {'username': 'corey', 'password': 'testing'}
r = requests.post('https://httpbin.org/post', params=payload)
# print(r.text) # we can use json method instead

r_dic = r.json()

print(json.dumps(r_dic, indent=2, sort_keys=True))


# r = requests.get('http://httpbin.org/delay/6', timeout=3)
