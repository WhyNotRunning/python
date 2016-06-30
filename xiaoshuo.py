


from urllib import request,error,parse
from bs4 import BeautifulSoup

import re
from datetime import datetime
from http import cookiejar,cookies

values = {'name' : 'Michael Foord', 'location' : 'pythontab', 'language' : 'Python' } 
url_values = parse.urlencode(values).encode(encoding='utf-8')
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36'}

req = request.Request('http://192.168.0.197:8080/drawback/home',url_values)
req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
req.add_header('Content-Type', 'application/x-www-form-urlencoded')
req.add_header('Cache-Control', 'no-cache')
req.add_header('Accept', '*/*')
req.add_header('Connection', 'Keep-Alive')
response = request.urlopen(req)
if response:
	print('success')

cookies = cookiejar.CookieJar()
#cookies.set_cookie()
opener = request.build_opener(request.HTTPCookieProcessor(cookies))
request.install_opener(opener)
response = request.urlopen(req)
for item in cookies:
    print('Name = '+item.name)
    print('Value = '+item.value)
print(response.getcode())
print(cookies)
print(response.read())