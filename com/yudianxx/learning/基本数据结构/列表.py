#!/usr/bin/env python
# -*- coding: utf-9 -*-
# @Time    : 2021/2/17 0:03
# @Author  : 醋酸菌HaC
# @Site    : https://rain.baimuxym.cn
# @File    : 列表.py

list1 = ['physics', 'chemistry', 1997, 2000]
list2 = [1, 2, 3, 4, 5, 6, 7]

print "list1[0]: ", list1[0]
# 左开右闭
print("list2[1:5]: ", list2[1:5])  # [2, 3, 4, 5]

# 2.
list = []  ## 空列表
list.append('Google')  ## 使用 append() 添加元素
list.append('Runoob')
print("list--->>>", list)

# 删除
del list[0]
print("list--->>>", list)
print(len(list))

# 3.
tup1 = (12, 34.56)
tup2 = ('abc', 'xyz')

# 以下修改元组元素操作是非法的。
# tup1[0] = 100

# 创建一个新的元组
tup3 = tup1 + tup2
print(tup3)

print(min(tup1))
print(min(tup2))
# 报错，int 和 string 不能比较
print(min(tup3))

# 4、判断列表是否存在某个元素

name = 2
if name in list:
    print("存在")
else:
    print("不存在")

# 5、api

list2.reverse()  # 升序
list2.sort(reverse=True)  # 降序

school = [[1, 2], [3, 4, 5], [6]]




# 使用 枚举拿到列表的k、v

mylist = ["a","b",0,2,3]


# 通过枚举拿到
for index,value in enumerate(mylist):
    print("下标:%s，值:%s"%(index,value))
