# -*- encoding: utf-8 -*-
'''
@File : ss.py
@Time : 2020/03/08 16:04:14
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
#!/usr/bin/python3

# 5  写函数，检查传入字典的每一个value长度，
# 如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者;

def dic(dict1):
    for x,y in dict1.items():
        if len(y)>2:
            i=y[0:2]
            dict1[x]=i
    return dict1

dict2=eval(input("请输入：")) # value不为数字，可为列表等
print(dic(dict2))
