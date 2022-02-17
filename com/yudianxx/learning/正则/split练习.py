# -*- coding: utf-8 -*-  解决中文注释的报错问题
import re

matchObject = re.split('a*', 'hello world')  # 对于一个找不到匹配的字符串而言，split 不会对其作出分割

# 对于找不到的，不会切割，会返回整个字符串的数组
print matchObject

matchObject2 = re.split('\W+', ' runoob, runoob, runoob.jb_abc', 1) # \W 是非字母数字
print matchObject2

# \W 是非字母数字及下划线,这里是任意非字母数字下划线后面加一个任意字符
matchObject3 = re.split('\W.', ' ,,runoob, runoob, runoob.jb_abc')
print  matchObject3