# -*- coding: UTF-8 -*-
# !/usr/bin/python
# import requests
#
# r = requests.get('http://cuiqingcai.com')
# print type(r)
# print r.status_code
# print r.encoding
# print r.cookies

import requests

url = 'http://httpbin.org/post'
files = {'file': open('test.txt', 'rb')}
r = requests.post(url, files=files)
print r.text
     