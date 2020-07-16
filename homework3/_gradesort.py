# -*- encoding: utf-8 -*-
'''
@File : 0.py
@Time : 2020/03/23 00:20:58
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
#!usr/bin/python3
# -*- coding: UTF-8 -*-

# 3 编写一个程序，读取文件中保存的10个学生成绩名单信息
# (学号,姓名, Python课程分数); 
# 然后按照分数从高到低进行排序输出

list=[]
with open("homework3\\grade.txt", "r",encoding='utf-8') as f:
    for line in f.readlines():
        list.append(line.strip().split())
print("排序前：")
for i in list:
    print(i)

list.sort(key=lambda k: k[2], reverse=True)
print("排序后：")
for i in list:
    print(i)