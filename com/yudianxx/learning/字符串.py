#!/usr/bin/python
# -*- coding: UTF-8 -*-
a = "Hello"
b = "Python"

print "a + b 输出结果：", a + b
print "a * 2 输出结果：", a * 2
# 可以直接是数组类型，不像Java，灵活得很
# python 的list也是可以这样的
print "a[1] 输出结果：", a[1]
print "a[1:4] 输出结果：", a[1:4]

if ("H" in a):
    print "H 在变量 a 中"
else:
    print "H 不在变量 a 中"

if ("M" not in a):
    print "M 不在变量 a 中"
else:
    print "M 在变量 a 中"
# R、r 表示输出原始字符
print r'\n'
print R'\n'


# 格式化
print ("格式化")
print ("My name is %s and weight is %d kg!" % ('Zara', 21) )

# 统计某个元素在列表中出现的次数
print (a.count("l"))

print (r"\n\tRr")

# 引号前小写的"u"表示这里创建的是一个 Unicode 字符串。
print u'\u6b22\u8fce\u8bbf\u95ee\u83dc\u9e1f\u6559\u7a0b\uff01'