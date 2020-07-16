# -*- encoding: utf-8 -*-
'''
@File : work3.py
@Time : 2020/03/08 10:02:03
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
#!/usr/bin/python3

# 7  随机生成20个学生的成绩; 判断这20个学生成绩的等级; 用函数来实现;  
#     A---成绩>=90;  
#     B-->成绩在 [80,90)
#     C-->成绩在 [70,80)
#     D-->成绩<70

from random import randint

data1=[randint(0,100) for x in range(20)]
print("学生成绩为：")
print(data1)

def level(data2):
    res=[]
    for i in data2:
        if i>=90:
            res.append('A')
        elif i>=80 and i<90:
            res.append('B')
        elif i>=70 and i<80:
            res.append('C')
        else:
            res.append('D')
    return res

print("对应等级为：")
print(level(data1))        