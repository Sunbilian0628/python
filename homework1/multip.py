# -*- encoding: utf-8 -*-
'''
@File : 02.py
@Time : 2020/03/08 00:52:01
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
#!/usr/bin/python3

# 7 打印输出9*9乘法表，按照下面的格式

for i in range(1,10):
    for j in range(1,10):
        if j<=i:
            print(j,"*",i,"=",i*j,end="  ")
        else:
            break
    print()
        