# -*- encoding: utf-8 -*-
'''
@File : 00.py
@Time : 2020/03/26 00:09:20
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

# 4  (继续上面的练习) 模拟用户登录:
#      5个同学的姓名,账号和密码(加密后的),保存在一个文件上;   
#      系统提示,请输入登录同学姓名, 正确后,请输入账号, 
#      正确后,提示请输入密码（输入明文）;  
#      如果都正确,打印提示, 您登录成功(失败);

import os
import hashlib

list1=[]
a=[]

with open('homework4\\work.txt', 'r',encoding='utf-8') as f:
    line = f.readlines()
    for i in line:
        list = i.strip().split()
        a.append(list)
        list1.append(i[0])

name = input('请输入姓名：\n')

for j in a:
    if j[0] == name:
        account = input('请输入账号:\n')
        if j[1] == account:
            h = hashlib.md5()
            password = input('请输入密码：\n')
            h.update(password.encode('utf-8'))
            if j[2] == h.hexdigest():
                print('您登陆成功！')
            else:
                print('密码错误！')
        else:
            print('账号输入错误！')
if name not in list1:
        print('未找到此人！')