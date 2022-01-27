#!/user/bin/python
# -*- coding: utf-8 -*-
import json

import requests

# 明星名字
pageFrom = 0
pageSize = 120
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"
}
flag = True
i = 1

while flag:
    url = "https://sp1.baidu.com/8aQDcjqpAAV3otqbppnN2DJv/api.php?resource_id=28266&frpnom_mid=1&&format=json&ie=utf-8&oe=utf-8&query=" \
          "中国明星&sort_key=&sort_type=1&stat0=&stat1=&stat2=&stat3=&pn=" \
          + str(pageFrom) + "&rn=" + str(pageSize)

    print "正在进行第" + str(i) + "次爬虫，url=" + url

    response = requests.get(url, headers)

    responseJson = json.dumps(response.json(), ensure_ascii=False)

    s = json.loads(responseJson)

    print s.keys()

    print responseJson

    pageFrom += pageSize;

    flag = False
