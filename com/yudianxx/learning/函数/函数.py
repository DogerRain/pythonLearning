#! / usr / bin / python
# -*- coding: UTF-8 -*-


# 可写函数说明
# 加了星号（*）的变量名会存放所有未命名的变量参数。不定长参数
def printinfo(arg1, *vartuple):
    "打印任何传入的参数"
    print("输出: ")
    print("arg1:", arg1)
    for var in vartuple:
        print(var)
    return


# 调用printinfo 函数
printinfo(10)
# 第一个是参数1，第一个之后的是可变参数2
printinfo(70,    60, 50)

printinfo("info")

