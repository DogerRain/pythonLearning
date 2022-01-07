#!/user/bin/python
# -*- coding: utf-8 -*-

import requests

siteUrl ="https://rain.baimuxym.cn/article/5"

# 发生GET类型请求
r_get = requests.get(siteUrl)

print("返回码：",r_get.status_code)
print "返回值：",r_get.text


