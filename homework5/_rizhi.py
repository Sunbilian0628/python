# -*- encoding: utf-8 -*-
'''
@File : 02.py
@Time : 2020/04/06 20:30:53
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib


# 2  编写一个装饰器，能记录其他函数调用的日志，将日志写入到文件中；

import os

def _applica(func):
    def datext(*args,**karg):
        func(*args,**karg)
        with open("homework5\\rizhi.txt", "a",encoding='utf-8') as f:
            f.write('{}'.format(func))
            f.write('\n')
        with open("homework5\\rizhi.txt", "r",encoding='utf-8') as f1:
            line = f1.readlines()
            for i in line:
                print(i)
    return datext

@_applica
def add(a, b):
    print('和为：{}'.format(a+b))

@_applica
def dis(a, b):
    print('和为：{}'.format(a-b))

a = int(input('第一个数：'))
b = int(input('第二个数：'))
c = input('请输入运算符：')
if c == '+':
    add(a,b)
if c == '-':
    dis(a,b)