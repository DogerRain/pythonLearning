#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/2/20 23:48
# @Author  : 醋酸菌HaC
# @Site    : https://rain.baimuxym.cn
# @File    : 豆瓣爬虫.py


from bs4 import BeautifulSoup ;

soup = BeautifulSoup(open('index.html'))  #使用本地文件创建对象

print(soup)