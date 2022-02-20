#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/2/20 16:47
# @Author  : 醋酸菌HaC
# @Site    : https://rain.baimuxym.cn
# @File    : 异常.py


# try:
#     f = open("123.txt", "r")
#     print(num)
# except IOError:
#     print("捕获异常")
# except EnvironmentError:
#     print("环境错误")
# except NameError:
#     print("未定义变量错误") # 只有一个错误捕获了，因为下面就不会执行了~

try:
    f = open("123.txt", "r")
    print("上面错误我还执行")
    # print(num)
except (IOError,NameError) as result:
    print("捕获异常:\n",result)
except Exception as result:
    print("捕获异常Exception")
finally:
    f.close()
    print("结束")