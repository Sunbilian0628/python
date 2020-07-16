# -*- encoding: utf-8 -*-
'''
@File : sd.py
@Time : 2020/03/08 15:53:29
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
#!/usr/bin/python3

# 4 写函数，统计字符串中有几个字母，几个数字，几个空格，几个其他字符，并返回结果

def words(str1):
    eng = 0
    num = 0
    kong = 0
    other = 0
    for i in str1:
        if i.isalpha():
            eng+=1
        elif i.isdigit():
            num+=1
        elif i.isspace():
            kong+=1
        else:
            other+=1
    return eng,num,kong,other

str2=input("请输入字符串：")
print("输出字符串中字母、数字、空格、其他字符的数量：")
print(words(str2))