# -*- encoding: utf-8 -*-
'''
@File : 0.py
@Time : 2020/03/26 00:16:39
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

# 8 京东二面笔试题
# 1） 生成一个大文件ip.txt,要求1200行，
# 每行随机为172.25.254.1---172.25.254.254之间的ip地址;
# 2） 读取ip.txt文件统计这个文件中ip出现频率排前10的ip

import random

def writefile():
    with open("homework4\\ip.txt", 'w',encoding='utf-8') as f:
        for i in range(0,1200):
            str1=random.randint(1,255)
            str2="172.25.254."+str(str1)
            f.write(str2+'\n')

def readfile():
    dict1 = {}
    with open("homework4\\ip.txt", "r",encoding='utf-8') as f1:
        list1=f1.readlines()
    for i in list1:
        if i in dict1:
            dict1[i] +=1
        else:
            dict1[i] = 1
    return dict1

def _sort(dict1):
    list1 = []
    values = sorted(dict1.items(),key=lambda x: x[1],reverse=True)
    values = values[:10]
    for i in values:
        list1.append(i[0])
    return list1

writefile()
dict1 = readfile()
list1 = _sort(dict1)
print('出现频率排前10的ip为：')
for i in list1:
    print(i)
