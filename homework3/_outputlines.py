# -*- encoding: utf-8 -*-
'''
@File : 0.py
@Time : 2020/03/22 23:49:28
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
#!usr/bin/python3
# -*- coding: UTF-8 -*-

# 2 写一个程序，从input.txt中读取之前输入的数据，
# 存入列表中，再加上行号打印显示；格式如下
# 第一行： xxxx
# 第二行： xxxx

import os

list=[]
with open("homework3\\input.txt", "r",encoding='utf-8') as f:
    list=f.readlines()

for i in list:
    print("第 {0} 行：{1}".format(list.index(i),i),end='')