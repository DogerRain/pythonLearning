# -*- coding: UTF-8 -*-
# !/usr/bin/python


import re

phone = "2004-959-559 # 这是一个国外电话号码"

#   # 开头到结束的任意字符 替换为 空
num = re.sub(r'#.*$', "", phone)
print "电话号码是: ", num

# 对比一下match 和 search
matchObj = re.match(r'\d+(.*)#.*$', phone)
matchObj1 = re.search(r'#.*$', phone)

if matchObj:
    print "matchObject:", matchObj.group()
if matchObj1:
    print "matchObject1:", matchObj1.group()

#  \D 表示 非数字，替换为 空
num = re.sub(r'\D', "", phone)
print "电话号码是 : ", num
