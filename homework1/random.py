# -*- encoding: utf-8 -*-
'''
@File : work.py
@Time : 2020/03/08 00:26:08
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
#!/usr/bin/python3

# 5  使用random模块，生成随机数，来初始化一个列表，元组；
#    使用了 random 模块的 randint() 函数来生成随机数，查询一下相关函数的用法

from random import randint

data1=[randint(-10,10) for x in range(5)]
print(data1)

data2=tuple([randint(-10,10) for x in range(5)])
print(data2)