#!/user/bin/python
# -*- coding: utf-8 -*-
import requests
headers ={
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"
}

# response = requests.get('https://www.csdn.net/community/toolbar-api/v1/get-user-info')
# 某个话题 https://www.zhihu.com/question/29925879
response = requests.get('https://www.zhihu.com/hot',headers=headers)
print type(response.status_code), response.status_code
print(type(response.headers), response.headers)
print(type(response.cookies), response.cookies)
print(type(response.url), response.url)
print(type(response.history), response.history)