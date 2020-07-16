# -*- encoding: utf-8 -*-
'''
@File : 04.py
@Time : 2020/04/26 10:40:47
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

# 4 多进程通讯：
#   编写一个简单的聊天程序；其中一个进程发送文字聊天消息（从键盘输入文字消息）；  
#   另外一个进程接收并打印消息

import os
import time
import random
from multiprocessing import Process
from multiprocessing import Queue

def write(a, queue):
    time.sleep(random.random())
    print('正在写入...')
    queue.put(a)
    print('写入完成')
    time.sleep(random.random())

def read(queue):
    while True:
        if not queue.empty():
            a = queue.get(True)
            print('正在读出数据...')
            print('取得输入数据为：')
            print(a)
            time.sleep(random.random())
        else:
            break

if __name__=='__main__':
    queue = Queue()
    t2 = Process(target=read, args=(queue,))
    while(True):
        a = input('请输入要发送的信息：')
        t1 = Process(target=write, args=(a, queue))
        t1.start()
        t1.join()
        flag = int(input('是否继续输入（1为继续，0为停止）：'))
        if flag == 0:
            break
    t2.start()
    t2.join()
    print('通信完成')