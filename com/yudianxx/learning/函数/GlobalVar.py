#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/2/20 16:33
# @Author  : 醋酸菌HaC
# @Site    : https://rain.baimuxym.cn
# @File    : GlobalVar.py

# 全局变量

a = 100


def printA():
    a = 200
    print(a)  # 默认使用全局变量，如果局部有，则使用局部


print("局部变量 a：", a)  # 局部变量无法修改全局变量


def editGlobalVar():
    global a
    a = 200
    print(a)


editGlobalVar()
print("局部变量 a：", a)
