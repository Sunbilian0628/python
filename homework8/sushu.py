# -*- encoding: utf-8 -*-
'''
@File : 03.py
@Time : 2020/04/26 10:40:54
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

# 3  多进程练习：
# 计算1～100000之间所有素数的个数， 要求如下:
# - 编写函数判断一个数字是否为素数，然后统计素数的个数；
# -对比1: 对比使用多进程和不使用多进程两种方法的统计速度。
# -对比2：对比开启4个多进程和开启10个多进程两种方法的速度。

import time
from multiprocessing import Process

# 判断某个数是否是素数
def sushu(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2, n):
            if n%i == 0:
                return False
        return True

# 不用进程时计算
def com1():
    start = time.time()
    list = []
    for i in range(1, 100000):
        if sushu(i):
            list.append(i)
    end = time.time()
    print(len(list))
    print('对比1不使用多进程%.2f' %(end-start))

# 进程类
class threadlei(Process):
    def __init__(self, list, i, j):
        super(threadlei, self).__init__()
        self.list = list
        self.i = i
        self.j = j

    def run(self):
        for k in range(self.i, self.j):
            if sushu(k):
                self.list.append(k)
        print(len(self.list))

def com2():
    flag = 0
    list1 = []
    list2 = []
    start1 = time.time()
    for i in range(0,4):
        t = threadlei(list1, flag, flag+25000)
        flag +=25000
        list2.append(t)
        t.start()
    for j in list2:
        j.join()
    end1 = time.time()
    print('对比1使用多进程%.2f' %(end1-start1))
    print('对比2使用4个多进程%.2f' %(end1-start1))

def com3():
    flag = 0
    list1 = []
    list2 = []
    start1 = time.time()
    for i in range(0,10):
        t = threadlei(list1, flag, flag+10000)
        flag += 10000
        t.start()
        list2.append(t)
    for j in list2:
        j.join()
    end1 = time.time()
    print('对比2使用10个多进程%.2f' %(end1-start1))

if __name__ == "__main__":
    com1()
    com2()
    com3()