#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/2/20 16:36
# @Author  : 醋酸菌HaC
# @Site    : https://rain.baimuxym.cn
# @File    : 文件操作.py


# f = open("PythonText.txt")

# f = open("PythonText.txt","w") # w，写模式；文件不存在则新建，默认当前目录
# f.write("I am 醋酸菌")
# f.close()


r = open("PythonText.txt", "r")  # 只读

# 读一行，会记住位置，再读会从下一行开始
content = r.readline()
r.close()
print(content)

r = open("PythonText.txt", "r")  # 只读
# 读多行
contents = r.readlines()
r.close()
print(contents)

# for
for line in contents:
    # end="" 表示不换行
    print("line:", line, end="")


