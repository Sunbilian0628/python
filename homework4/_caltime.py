# -*- encoding: utf-8 -*-
'''
@File : 03.py
@Time : 2020/03/26 00:04:34
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

# 2 定义一个函数，判断一个输入的日期，是当年的第几周，周几？  
# 将程序改写一下，能针对我们学校的校历时间进行计算
# （校历第1周，2月17-2月23；校历第27周，8月17-8月23；）

from datetime import datetime

input1 = input('请输入要判断的日期（例：20000216）\n')

week = datetime.strptime(input1,"%Y%m%d").strftime("%W")
print('输入的日期是第{}周\n'.format(week))

print('改写程序\n')

week1 = datetime.strptime('20200217',"%Y%m%d").strftime("%W")
input2 = eval(input('请输入要判断的日期（例：20000216）\n'))
if input2>=20200217 and input2<=20200823:
    input2=str(input2)
    week2 = datetime.strptime(input2,"%Y%m%d").strftime("%W")
    week1=int(week1)
    week2=int(week2)
    print('输入的日期是第{}周\n'.format(week2-week1))
else:
    print('输入日期不在本学期校历中')