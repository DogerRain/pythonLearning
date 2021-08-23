#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests

# url = "http://10.128.19.235:8080/admin/task/findall"
#
# payload={}
# headers = {}
#
# response = requests.request("POST", url, headers=headers, data=payload)
#
# print(response.text)
import sys
reload(sys)
sys.setdefaultencoding('utf8')

url = "http://10.128.19.235:8080/admin/download/fileAndPage/summary"
province = '"广东省","北京市"'.encode("utf-8")
payload='taskId=34&startDate=2021-08-01 00:00:00&endDate=2021-08-04 00:00:00&timeInterval=120&province='+province
print payload
headers = {
  'Content-Type': 'application/x-www-form-urlencoded'
}

# payload=payload.encode('GBK')

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
