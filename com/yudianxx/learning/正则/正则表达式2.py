# #导入re模块
# import re
#
# # 将正则表达式编译成Pattern对象
# pattern = re.compile(r'world')
# # 使用search()查找匹配的子串，不存在能匹配的子串时将返回None
# # 这个例子中使用match()无法成功匹配
#
# match = re.search(pattern,'hello world!')
# if match:
#     # 使用Match获得分组信息
#     print(match.group())
#  # 输出
# # world


import re
# + 表示匹配 表示至少一个字符
pattern = re.compile(r'\d+')
# 以匹配到的pattern为分隔符
match = re.search(pattern,'122one1two2three3four4')
print(match.group())

print( re.split(pattern,'122one1two2three3four4'))

### 输出 ###
# ['one', 'two', 'three', 'four', '']



import re

pattern = re.compile(r'\d+')
for m in re.finditer(pattern,'one11two2three3four4'):
    print( m.group()),

### 输出 ###
# 1 2 3 4