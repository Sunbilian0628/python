# -*- encoding: utf-8 -*-
'''
@File : 01.py
@Time : 2020/03/26 00:11:11
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

# 6 通过Python来实现显示给定文件夹下的所有文件和文件夹,
# 以及时间，如果是文件，显示大小; 
# 输出格式效果如下:
# 名称     日期     类型（文件夹或者 文件）     大小

import os
import time

def _sumsize(s):
    sum = 0
    for root,dirs,files in os.walk(s):
        for f in files:
            sum += os.path.getsize(os.path.join(root, f))
    return ('%.2f' %(sum/float(1024*1024)))
 
def _time(s):
    filemt = time.localtime(os.stat(s).st_mtime)
    return time.strftime("%Y-%m-%d", filemt)

filepath = os.getcwd()
list1 = os.listdir(filepath)
list2=[]

for i in list1:
    j = filepath+"\\"+i
    if os.path.isfile(j):
        list4 = []
        list4.append(i)
        list4.append(_time(j))
        list4.append("文件")
        size = os.path.getsize(j)
        str1 = str('%.2f' %size/float(1024*1024))
        list4.append(str1)
        list2.append(list4)
    else:
        list4 = []
        list4.append(i)
        list4.append(_time(j))
        list4.append("文件夹")
        str1 = str(_sumsize(j))
        list4.append(str1)
        list2.append(list4)

print('名称         日期                类型         大小')
for i in list2:
    print(i[0].ljust(13)+i[1].ljust(20)+i[2].ljust(10)+i[3].ljust(10))