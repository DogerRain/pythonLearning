# -*- coding:UTF8 -*-

import re
# + 表示至少一个字符
pattern = re.compile(r'\d{2}')  # 查找数字，表示只有两个数字的
result1 = pattern.findall('runoob 123 google 456 18898')

# result1 = pattern.match('runoob 123 google 456 1', 0, 100)
#
result2 = pattern.findall('run88oob123google456', 0, 10)

print(result1)
print(result2)
