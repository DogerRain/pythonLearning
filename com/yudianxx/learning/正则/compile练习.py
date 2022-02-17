#-*- coding: utf-8 -*-  解决中文注释的报错问题
import re
# * 是任意个字符，这里表示 后面任意个\D 即任意个非数字
#pattern = re.compile(r'\d{1,2}\D*')
# . 是一个任意字符（表示一个）
# pattern = re.compile(r'\d{1,2}\D*')
#  任意个非数字 再接 一个任意字符（.表示 一个）
# pattern = re.compile(r'\d{1,2}\D*\d*.')
#
# matchObject = pattern.match('one12twothree345four56five', 3, 201) #  从3开始（含）到 201（不含）
#
#
# if  matchObject:
#     print matchObject.group()
# else:
#     print "没有匹配到"
#
#
# pattern = re.compile(r"^h\D{3}o")
#
# matchObject = pattern.match("hello world hallo")
#
# if  matchObject:
#     print matchObject.groups()
#     print matchObject.group()
# else:
#     print "nothing"
#


# pattern = re.compile(r"cdn")
# pattern = re.compile(r".*^/(1,).*")

str = "https://cdn.jsdelivr.net/gh/DogerRain/image@main/img-202109/6555006-1f81e81466729c6b.png"
# matchObject = pattern.match(str)
#
# if matchObject:
#     # print matchObject.groups()
#     print matchObject.group()
#     # print matchObject.group(1)
# else:
#     print "nothing"




pattern = re.compile(r"https?://(.*)")
# matchObject = pattern.match(url)
matchObject = pattern.findall(str)
if matchObject:
    print matchObject
else:
    print "nothing"



matchObj = re.search(r'//(.*)/', str, re.M | re.I)
if matchObj:
    print "search --> searchObj.group() : ", matchObj.group()
else:
    print "No match!!"



