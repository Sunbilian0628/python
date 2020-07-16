# -*- encoding: utf-8 -*-
'''
@File : work3.py
@Time : 2020/03/08 00:05:11
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
#!/usr/bin/python3

# 3 定义2个列表，并初始化；  找出这2个列表中，相同的元素并输出

list1=[1,5,8,4,3,11]
list2=[5,8,11,12,15,16]
for i in list1:
    for j in list2:
        if i==j:
            print(i,end=" ")