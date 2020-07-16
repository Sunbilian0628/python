# -*- encoding: utf-8 -*-
'''
@File : 01.py
@Time : 2020/04/19 19:35:52
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

# 1 给定一个文件，请用正则表达式，逐行匹配提取其中的URL链接信息，
# 并保存到另外一个文件中；
# 提示，文件有1000行，注意控制每次读取的行数；

import os, re

def getinfor():
    with open("homework7//web.txt", 'r', buffering=1, encoding='utf-8')as f:
        line = f.read()
    obj=re.findall(r'http://[a-zA-Z0-9\.-\u4e00-\u9fa5]+\.[com|cn|org|net]*',line)
    with open("homework7//webcopy.txt", 'w', encoding='utf-8')as f2:
        for i in obj:
            f2.write(i+'\n')
#http://www\.[a-zA-Z0-9]*\.[0-9\u4e00-\u9fa5]*\.[com|cn|org|net]{1,3}
# http://[a-zA-Z0-9\.\-\u4e00-\u9fa5]+

if __name__ == '__main__':
    getinfor()