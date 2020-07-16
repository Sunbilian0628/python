# -*- encoding: utf-8 -*-
'''
@File : asd.py
@Time : 2020/03/08 15:24:45
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
#!/usr/bin/python3

# 2 编写一个函数,接收n个数字，求这些参数数字的和

#方法一
# def _sum(a):
#     return sum(a)

# s=eval(input("请输入数字："))
# print(_sum(s))

#方法二
def sum_func(n):
    sm = 0
    for i in range(0,n):
        a=int(input("第{}个数是：".format(i+1)))
        sm += a
    return sm

n=int(input("请输入n的值："))
print("请依次输入n个值：")
print("和为：{}".format(sum_func(n)))