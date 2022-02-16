#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/2/17 0:03
# @Author  : 醋酸菌HaC
# @Site    : https://rain.baimuxym.cn
# @File    : 列表.py


mylist = ["a","b",1,2,3]


# 通过枚举拿到
for index,value in enumerate(mylist):
    print("下标:%s，值:%s"%(index,value))