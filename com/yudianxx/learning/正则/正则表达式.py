# -*- coding:UTF8 -*-
import re

m = re.match(r'(\w+) (\w+)(?P<sign>.*)', 'hello world!')
print(m.group())

# 将正则表达式编译成Pattern对象
# pattern = re.compile(r'^h[a-zA-Z!\s]*')
pattern = re.compile(r'@[a-zA-Z0-9]*')

# 使用Pattern匹配文本，获得匹配结果，无法匹配时将返回None
str = "huangyongweg0306@163.com"
# str = "hello world!"
match = pattern.match(str)

if match:
    # 使用Match获得分组信息
    print(match.group())

### 输出 ###
# hello


__author__ = 'CQC'

# -*- coding: utf-8 -*-

# 导入re模块
import re

# 将正则表达式编译成Pattern对象，注意hello前面的r的意思是“原生字符串”
pattern = re.compile(r'hello')

# 使用re.match匹配文本，获得匹配结果，无法匹配时将返回None
result1 = re.match(pattern, 'hello')
result2 = re.match(pattern, 'helloo CQC!')
result3 = re.match(pattern, 'helo CQC!')
result4 = re.match(pattern, 'hello CQC!')

# 如果1匹配成功
if result1:
    # 使用Match获得分组信息
    print(result1.group())
else:
    print('1匹配失败！')

# 如果2匹配成功
if result2:
    # 使用Match获得分组信息
    print(result2.group())
else:
    print('2匹配失败！')

# 如果3匹配成功
if result3:
    # 使用Match获得分组信息
    print(result3.group())
else:
    print('3匹配失败！')

# 如果4匹配成功
if result4:
    # 使用Match获得分组信息
    print(result4.group())
else:
    print('4匹配失败！')


