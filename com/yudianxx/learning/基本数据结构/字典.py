#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/2/16 23:36
# @Author  : 醋酸菌HaC
# @Site    : https://rain.baimuxym.cn
# @File    : 字典.py

# 无序集合，使用 k-v 形式，key必须是唯一


dict = {"name": "醋酸菌", "age": 18}

dict2 = {"醋酸菌", "HaC", 12}

print(dict)
print(dict["name"])

# 访问不存在的元素会报错，可以使用get，会显示none
print(dict.get("name1"))
print(dict.get("name1", "吴彦祖"))  # 为空的默认值

print(dict2)

# 增
dict["sex"] = "男"
print(dict)
# 删，删除的是 键值对
del dict["sex"]

print("删：%s" % dict)


# 改
dict["name"] ="HaC"
print("改：",dict)


# 查
print("遍历：")
print(dict.keys())
print(dict.values())
print(dict.items())
for key in dict.keys():
    print(key)

for key,value in dict.items():
    print("key =",key , ",value =",value)

# 清空
# del dict  这个是删除整个字典，删除了就没有了
dict.clear()
print(dict)


# 合并

dict3  = dict2.update(dict2)

print(dict3)