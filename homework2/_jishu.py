# -*- encoding: utf-8 -*-
'''
@File : dxaj.py
@Time : 2020/03/08 15:39:33
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
#!/usr/bin/python3

# 3  编写一个函数, 传入一个数字列表, 输出列表中的奇数;
#    数字列表请用随机数函数生成

from random import randint

data1=[randint(-10,10) for x in range(5)]
print("原列表为：{}".format(data1))

def jishu(data):
    res=filter(lambda x: x%2 != 0,data1)
    return res
    
print("筛选后的列表为：{}".format(list(jishu(data1))))