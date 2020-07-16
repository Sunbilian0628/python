# -*- encoding: utf-8 -*-
'''
@File : 04.py
@Time : 2020/03/26 00:07:58
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

# 3  从键盘输入5个同学的账号和密码,然后将他们的姓名,
# 账号和密码(密码需要加密)保存到一个文件中;

import os
import hashlib

with open("homework4\\work.txt",'w',encoding='utf-8') as f:
    for i in range(0, 5):
        name = input('请输入姓名：\n')
        account = input('请输入账号：\n')
        h = hashlib.md5()
        passwordstr = input('请输入密码：\n')
        h.update(passwordstr.encode('utf-8'))
        f.write(name+"   "+account+"   "+h.hexdigest())
        f.write('\n')
        print('-----------------------------------------------')

with open("homework4\\work.txt",'r',encoding='utf-8') as f1:
    line=f1.readlines()
    for i in line:
        j,k,l = i.split()
        print(j+"  "+k+"  "+l)