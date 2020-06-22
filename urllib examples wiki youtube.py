# https://en.wikipedia.org/wiki/URL?key=value&life=42#History - Uniform resource location URL
# protocal: http, https, ftp, ...
# Host: en.wikipedia.org
# Port: http=80, https = 443
# path: wiki/URL
# Querystring: key-value&life=42
# Fragment: History
# urllib  #python3 contains request (open URLs), response, error, parse (useful URL functions), robotparser (robots.txt files)


from urllib import request
from urllib import parse

print(request)



# resp = urllib.request.urlopen('http://www.wikipedia.org/')
# print(type(resp))
# print(resp.code)
# print(resp.length)
# print(resp.peek())
# data = resp.read()
# html = data.decode("UTF-8")
# #print(html)

# Youtube example
params = {'v': "EuC-yVzHhMI",'t':"5m56s"}
querystring = parse.urlencode(params)
print(querystring)
url = "https://www.youtube.com/watch" + "?" + querystring
resp = request.urlopen(url)
print(resp.isclosed())
print(resp.code)
html = resp.read().decode("utf-8")
print(html[:500])
