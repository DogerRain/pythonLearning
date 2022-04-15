#-*- coding: utf-8 -*-  解决中文注释的报错问题
import re
line = "Cats are smarter than dogs"

## than 开头的字符串
matchObj = re.match(r'than(.*)s', line, re.M | re.I)
if matchObj:
    print "match --> matchObj.group() : ", matchObj.group()
else:
    print "No match!!"


matchObj = re.search(r'than(.*)s', line, re.M | re.I)
if matchObj:
    print "search --> searchObj.group() : ", matchObj.group()
else:
    print "No match!!"



# 区别：re.match只匹配字符串的开始，如果字符串开始不符合正则表达式，则匹配失败，函数返回None；
# 而re.search匹配整个字符串，直到找到第一个匹配。 左闭右开 [4,6)；re.serarch("aa","abcaabaa")