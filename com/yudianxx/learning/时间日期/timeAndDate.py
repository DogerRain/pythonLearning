#!/usr/bin/python
# -*- coding: UTF-8 -*-

import time
import calendar
import datetime

print ("time.localtime():",time.localtime())
# 格式化成2016-03-20 11:45:39形式
print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

# 格式化成Sat Mar 28 22:24:24 2016形式
print time.strftime("%a %b %d %H:%M:%S %Y", time.localtime())


# print time.strftime("%Y-%m-%d %H:%M:%S",  "2016-03-20 11:45:39")


# 将格式字符串转换为时间戳
a = "Sat Mar 28 22:24:24 2016"
print time.mktime(time.strptime(a, "%a %b %d %H:%M:%S %Y"))

year = 2021
month = 8
cal = calendar.month(year, month)
print ("以下输出 %d 年 %d 月份的日历:" % (year, month))
print cal

timeZone = time.localtime()
print timeZone
print datetime.timedelta(hours=23, minutes=59, seconds=59)