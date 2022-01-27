#!/usr/bin/python
# -*- coding: utf-8  -*-

class listTest():

    def __init__(self, name="醋酸菌"):
        print("来了，",name,"老弟")
        print "来了老弟"+name

    def listFun(self):
        mylist = ['Google', 'Yahoo', 'Baidu']
        mylist[1] = 'Microsoft'
        print(mylist)


if __name__ == "__main__":
    # 这里相对于Java的构造函数，默认就是调用 __init__ 方法
    # listObject = listTest()
    # listObject.listFun()
    listTest("大木菌").listFun()
