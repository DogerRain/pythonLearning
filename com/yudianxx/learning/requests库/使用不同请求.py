#!/user/bin/python
# -*- coding: utf-8 -*-

import requests

siteUrl = "https://rain.baimuxym.cn/article/5"
data = {
    'name': 'germey',
    'age': 22
}

# 发生GET类型请求
# result_get  = requests.get(siteUrl, params=data)

# result_post = requests.post("http://httpbin.org/post",data=data)

# 返回值


response = requests.get('https://www.csdn.net/community/toolbar-api/v1/get-user-info')
print(type(response.status_code), response.status_code)
print(type(response.headers), response.headers)
print(type(response.cookies), response.cookies)
print(type(response.url), response.url)
print(type(response.history), response.history)

# 返回的不是json，会报错
print(response.json())
print(response.text)