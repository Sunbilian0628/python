# -*- encoding: utf-8 -*-
'''
@File : 0.py
@Time : 2020/03/22 21:38:18
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
#!usr/bin/python3
# -*- coding: UTF-8 -*-

# 1 写一个程序，读取键盘输入的任意行文字信息，
# 当输入空行时结束输入，将读入的字符串存于列表;
# 然后将列表里面的内容写入到文件input.txt中;

import os

list=[]
while True:
    str = input("请输入信息（最后以回车空行结束）：")
    if len(str) > 0:
        list.append(str)
    else:
        break

with open("homework3\\input.txt", "w",encoding='utf-8') as f:
    for line in list:
        f.write(line+'\n')