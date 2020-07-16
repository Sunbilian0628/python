# -*- encoding: utf-8 -*-
'''
@File : work4.py
@Time : 2020/03/08 00:14:23
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
#!/usr/bin/python3

# 4  判断用户输入的年份是否为闰年

x = int(input("请输入年份："))
if x%4 == 0:
    if x%100 == 0:
        if x%400 == 0:
            print("{}是闰年".format(x))
        else:
            print("{}不是闰年".format(x))
    else:
        print("{}是闰年".format(x))
else:
    print("{}不是闰年".format(x))