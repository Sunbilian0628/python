# -*- encoding: utf-8 -*-
'''
@File : 01.py
@Time : 2020/03/25 23:52:23
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

# 5  通过Python来模拟实现一个txt文件的拷贝过程;

import sys,os

# 可以实现任意类型的文件的拷贝

def copy(fpath,epath):
    list=[]
    if os.path.exists(fpath):
        with open(fpath,'r') as f:
            list=f.read()
            name=os.path.splitext(fpath)
            filename,type=name
        path=os.path.join(epath,'copy'+type)
        with open(path,'w') as f2:
            for i in list:
                f2.write(i)
    else:
        print('未找到文件')

path=os.getcwd()
path1=path+'//homework4//foo.txt'
copy(path1,'D://')