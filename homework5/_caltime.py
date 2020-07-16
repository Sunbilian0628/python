# -*- encoding: utf-8 -*-
'''
@File : 01.py
@Time : 2020/04/06 20:23:51
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib


# 1  编写一个装饰器，能计算其他函数的运行时间；

import time

def _applica(func):
    def caltime():
        starttime = time.time()
        func()
        endtime = time.time()
        alltime = ("%.6f" %(endtime - starttime))
        print("运行时间为{}".format(alltime))
    return caltime

@_applica
def staytime():
    time.sleep(3)
    print("hello world")

staytime()