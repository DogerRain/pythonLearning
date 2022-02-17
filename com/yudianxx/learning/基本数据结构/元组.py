#!/user/bin/python
# -*- coding: utf-8 -*-

tup =("abc","1234",123,0.23)

# 如果超过数组大小，并不会报错
print(tup[1:50]) # 左闭右开


print(tup[1])


# 元组修改是不允许的
# tup[2] = 12333

# 增

tup2=("醋酸菌",) # 这里需要给他用,注明是一个元组，不然它觉得是个字符串

tupNew = tup+tup2

print(tupNew)


# 删
# 不允许删

for i in tupNew:
    print(i)