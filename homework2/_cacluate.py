# -*- encoding: utf-8 -*-
'''
@File : xa.py
@Time : 2020/03/08 18:39:58
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
#!/usr/bin/python3

# 10 编写一个函数cacluate, 可以实现2个数的运算(加,减 乘,除)

def cacluate(a,m,b):
    if m == '+':
        return a+b
    elif m == '-':
        return a-b
    elif m == '*':
        return a*b
    elif m == '/':
        return a/b
    else:
        print("输入非法！")
        return


a=int(input("请输入第一个数："))
m=input("请输入运算符：")
b=int(input("请输入第二个数："))

if b == 0 and m == '/':
    print("输入非法！")
else:
    print("计算结果为：{}".format(cacluate(a,m,b)))