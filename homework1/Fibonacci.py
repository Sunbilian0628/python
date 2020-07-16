# -*- encoding: utf-8 -*-
'''
@File : 01.py
@Time : 2020/03/08 00:42:45
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
#!/usr/bin/python3

# 6  前面2个元素为0，1，输出100以内的斐波那契数列

def Fibonacci(n):
    if n == 0:
        return 0
    a, b = 0, 1
    for k in range(n + 1):
        a, b = b, a + b
    return a

for i in range(100):
    if Fibonacci(i)<=100:
        print(Fibonacci(i), end=' ')
    else:
        break