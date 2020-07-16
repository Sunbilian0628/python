# -*- encoding: utf-8 -*-
'''
@File : 01.py
@Time : 2020/04/25 21:12:12
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

# 1  有100个同学的分数：数据请用随机函数生成；
#      A  利用多线程程序（比如，5个线程，每个线程负责输出20条记录），
#      快速输出这100个同学的信息；
#      B 利用线程池来实现；

from random import randint
import threading
from concurrent.futures import ThreadPoolExecutor


def build():
    list = [randint(0,100) for i in range(0, 100)]
    return list

def func():
    for i in range(20):
        print(list.pop(i))

if __name__ == "__main__":
    list = build()
    pool = ThreadPoolExecutor(3)
    for i in range(0,5):
        task = pool.submit(func)