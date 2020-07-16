# -*- encoding: utf-8 -*-
'''
@File : ws.py
@Time : 2020/03/08 16:44:54
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
#!/usr/bin/python3

# 8  请用Python定义一个函数，给定一个字符串，
# 找出该字符串中出现次数最多的那个字符，
# 并打印出该字符及其出现的次数。
#  例如，输入 aaaabbc，输出：a:4

def string(str1):
    dic={}
    for i in str1:
        if i in dic.keys():
            dic[i]+=1
        else:
            dic[i]=1
    m=max(dic.values())
    for k,v in dic.items():
        if v == m:
            print("输出：{0}:{1}".format(k,v))

str1=input("输入：")
string(str1)