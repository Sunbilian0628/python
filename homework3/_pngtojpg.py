# -*- encoding: utf-8 -*-
'''
@File : 0.py
@Time : 2020/03/23 00:39:03
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
#!usr/bin/python3
# -*- coding: UTF-8 -*-

# 4 题目要求：
#  在当前目录新建目录img, 里面包含10个文件, 
#  10个文件名各不相同(X4G5.png)
#  将当前img目录所有以.png结尾的后缀名改为.jpg.

import os
import random
import string

# 创建文件夹
os.mkdir('img')
# 通过随机数产生文件名，其中.join函数为将随机出来的列表内元素合并
for i in range(10):
    str = random.sample(string.ascii_letters,4)
    str = ''.join(str)
    str2 = "img//" +str+ ".png"
    open(str2,'w')
# 以open方式创建文件

# 判断img是否创建成功
# 并在img的文件列表中找到以.png结尾的文件
# 将文件中除了.png的文件路径保存，重新赋予新的文件类型
if os.path.exists('img'):
    pngname = [i for i in os.listdir('img') if i.endswith('.png')]
    chname = [os.path.splitext(i)[0] for i in pngname]
    for j in chname:
        befoname = os.path.join('img', j+'.png')
        endname = os.path.join('img', j+'.jpg')
        os.rename(befoname,endname)