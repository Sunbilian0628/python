# -*- encoding: utf-8 -*-
'''
@File : 03.py
@Time : 2020/04/06 20:30:49
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib


# 3  编写一个装饰器，为多个函数加上认证的功能
# （必须输入用户的账号密码，才能调用这个函数）

import os
import hashlib

def _applica(func):
    def datext(*args,**karg):
        list1=[]
        a=[]
        with open('homework5\\work.txt', 'r',encoding='utf-8') as f:
            line = f.readlines()
            for i in line:
                list = i.strip().split()
                a.append(list)
                list1.append(i[0])
            account = input('请输入账号：\n')
            for j in a:
                if j[0] == account:
                    h = hashlib.md5()
                    password = input('请输入密码：\n')
                    h.update(password.encode('utf-8'))
                    if j[1] == h.hexdigest():
                        flag = 1
                    else:
                        flag = 0
                    if account not in list1:
                        flag = 0
        if flag == 1:
            print('认证成功！')
            func(*args,**karg)
        else:
            print('认证失败！')
    return datext

@_applica
def add(a, b):
    print('和为：{}'.format(a+b))

add(2,3)