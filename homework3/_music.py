# -*- encoding: utf-8 -*-
'''
@File : 0.py
@Time : 2020/03/23 09:34:41
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
#!usr/bin/python3
# -*- coding: UTF-8 -*-

# 5 文件编程小项目

import os

# 文件初始内容
list=[
    "How many roads must a man walk down",
    "Before they call him a man",
    "How many seas must a white dove sail",
    "Before she sleeps in the sand",
    "How many times must the cannot balls fly",
    "Before they're forever banned",
    "The answer my friend is blowing in the wind",
    "The answer is blowing in the wind"
]

# 创建文件，将初始化内容写入文件
with open("homework3\\Blowing in the wind.txt", "w",encoding='utf-8') as f:
    for i in list:
        f.writelines(i)
        f.write('\n')

# 在文件头部插入歌名
with open("homework3\\Blowing in the wind.txt", "r+",encoding='utf-8') as f:
    str1 = f.read()
    f.seek(0)
    str2="Blowin' in the wind\n"
    f.write(str2)
    f.write(str1)

# 在歌名后插入歌手名
list1=[]
with open("homework3\\Blowing in the wind.txt", "r",encoding='utf-8') as f:
    for i in f:
        list1.append(i)
str1="\t\tBob Dylan\n"
list1.insert(1,str1)
str2=''.join(list1)
with open("homework3\\Blowing in the wind.txt", "w+",encoding='utf-8') as f:
    f.write(str2)

# 在文件末尾加上字符串
with open("homework3\\Blowing in the wind.txt", "a",encoding='utf-8') as f:
    str3="1962 by Warner Bros.Inc"
    f.write(str3)

# 打印文件内容
with open("homework3\\Blowing in the wind.txt", "r",encoding='utf-8') as f:
    list2 = f.readlines()
    for i in range(0,len(list2)):
        if 1<i<len(list2)-1:
            print('\t'+list2[i])
        else:
            print('\t\t'+list2[i])