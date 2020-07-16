# -*- encoding: utf-8 -*-
'''
@File : 0.py
@Time : 2020/03/23 11:09:41
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
#!usr/bin/python3
# -*- coding: UTF-8 -*-

# 6  在2个文件中存放了英文计算机技术文章
# (可以选择2篇关于Python技术文件操作处理技巧的2篇英文技术文章), 
# 请读取文章内容,进行词频的统计;并分别输出统计结果到另外的文件存放;
# 比较这2篇文章的相似度(如果词频最高的前10个词,重复了5个,相似度就是50%;
# 重复了6个,相似度就是60% ,......);

import os

# 将文章中的单词提取出来放入字典中
def culcate(s):
    dict1 = {}
    with open(s, "r",encoding='utf-8') as f1:
        str1=f1.read()
    f1.close()
    for i in str1:
        if i in "~@#$%^&*()_-+=<>?/,.:;{}[]|\'""":
            str1=str1.replace(i,"")
    list1=str1.split()
    for i in list1:
        if i in dict1:
            dict1[i] +=1
        else:
            dict1[i] = 1
    return dict1

# 将前十位的出现次数最多的单词存入文件中
def _sort(dict1,s):
    list1 = []
    values = sorted(dict1.items(),key=lambda x: x[1],reverse=True)
    values = values[:10]
    with open(s, "w",encoding='utf-8') as f4:
        for i in values:
            f4.write(i[0]+'  '+str(i[1])+'\n')
            list1.append(i[0])
    return list1

# 判断文章的相似度
def _sumarticle(list2,list3):
    sum = 0
    for i in list2:
        if i in list3:
            sum = sum+1
    return sum

dict2=culcate("homework3\\artic1.txt")
dict3=culcate("homework3\\artic2.txt")

list2 = _sort(dict2,"homework3\\_cunart1.txt")
list3 = _sort(dict3,"homework3\\_cunart2.txt")

sum = _sumarticle(list2,list3)

# 输出
if sum >= 0 and sum <= 10:
    print("这两篇文章的相似度为：{}%".format(sum*10))