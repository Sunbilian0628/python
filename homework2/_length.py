# -*- encoding: utf-8 -*-
'''
@File : work1.py
@Time : 2020/03/08 10:01:37
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
#!/usr/bin/python3

# 1 写函数，判断用户传入的对象（字符串、列表、元组）长度,并返回给调用者

def _decide(s):
    return len(s)

a=eval(input("请输入数据："))
print(_decide(a))
