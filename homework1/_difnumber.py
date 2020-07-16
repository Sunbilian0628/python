# -*- encoding: utf-8 -*-
'''
@File : work1.py
@Time : 2020/03/05 22:28:22
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
#!/usr/bin/python3

# 1 元素输出和查找:请输出0-50之间的奇数，偶数，质数；能同时被2和3整除的数

for i in range(0,51):
    if i%2==0:
        print("偶数有：{}" .format(i))
    else:
        print("奇数有：{}" .format(i))

print("======================================")

for j in range(2,51):
    if j==2:
        print("质数有：{}" .format(j))
    for k in range(2,j):
        if j%k==0:
            break
        if k+1==j:
            print("质数有：{}" .format(j))

print("======================================")

for i in range(0,51):
    if i%2==0 and i%3==0:
        print("能被2和3整除的数有：{}" .format(i))