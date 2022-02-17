import re

str = "www.rainbaimuxym.cn"
print re.match('www', str).span()

print re.match('ww', str, re.M | re.I).group()

# !/usr/bin/python
import re

line = "Cats are smarter than dogs"

matchObj = re.match(r'(.*) are (.*)g(.*)', line, re.M | re.I)

if matchObj:
    print "matchObj.group() : ", matchObj.group()
    print "matchObj.group(1) : ", matchObj.group(1)
    print "matchObj.group(2) : ", matchObj.group(2)
    print "matchObj.group(2) : ", matchObj.group(3)
else:
    print "No match!!"


# 2
line = "Cats are smarter than dogs"

matchObj = re.search(r'(.*) are (.*)g(.*)', line, re.M | re.I)

if matchObj:
    print "matchObj.group() : ", matchObj.group()
    print "matchObj.group(1) : ", matchObj.group(1)
    print "matchObj.group(2) : ", matchObj.group(2)
    print "matchObj.group(2) : ", matchObj.group(3)
else:
    print "No match!!"

# 3. match 和 search 的区别：
# re.match只匹配字符串的开始，如果字符串开始不符合正则表达式，则匹配失败，函数返回None；而re.search匹配整个字符串，直到找到一个匹配。

# !/usr/bin/python
