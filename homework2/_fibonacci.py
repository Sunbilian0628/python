# -*- encoding: utf-8 -*-
'''
@File : w.py
@Time : 2020/03/08 16:20:27
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
#!/usr/bin/python3

# 6  定义一个函数, 打印输出n以内的斐波那契数列

def fibonacci(n):
    a,b=0,1
    res=[]
    while(a<n):
        res.append(a)
        a,b=b,a+b
    return res

n=int(input("请输入上限："))
print(fibonacci(n))