# -*- encoding: utf-8 -*-
'''
@File : 02.py
@Time : 2020/03/25 23:59:41
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

# 1 定义一个10个元素的列表，通过列表自带的函数，
# 实现元素在尾部插入和头部插入并记录程序运行的时间；
# 用deque来实现，同样记录程序所耗费的时间；
# 输出这2个时间的差值；
# 提示：列表原生的函数实现头部插入数据：list.insert(0, v)；list.append（2）

from collections import deque
import datetime

list1 = [10, 2, 21, 25, 18, 95, 94, 15, 41, 72, 88 ]
print(list1)

now1 = datetime.datetime.now()
list1.append('66')
list1.insert(0, '51')
now2 = datetime.datetime.now()
now3 = (now2-now1).microseconds
print("所用时间为：{}".format(now3))

print(list1)
print()
list2 = deque([10, 2, 21, 25, 18, 95, 94, 15, 41, 72, 88 ])
print(list2)

now1 = datetime.datetime.now()
list2.append('66')
list2.appendleft('51')
now2 = datetime.datetime.now()
now4 = (now2-now1).microseconds
print("所用时间为：{}".format(now4))

print(list2)

print("时间差为：{}".format(now4-now3))