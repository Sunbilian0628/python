# -*- encoding: utf-8 -*-
'''
@File : 0.py
@Time : 2020/03/26 00:15:04
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

# 7 使用python代码统计一个文件夹中所有文件的总大小

import os

def _sumsize(s):
    sum = 0
    for root,dirs,files in os.walk(s):
        for f in files:
            sum += os.path.getsize(os.path.join(root, f))
    return sum

f = os.getcwd()
f = f+"\\homework4"
sumsize=_sumsize(f)
sumsize = sumsize/float(1024*1024)
print("文件夹总大小为：%.2f MB" %(sumsize))