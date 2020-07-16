# -*- encoding: utf-8 -*-
'''
@File : 05.py
@Time : 2020/05/05 23:01:28
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
import socket
import threading
import os

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 获得本机地址
host = socket.gethostname()
ip = socket.gethostbyname(host)
addr = s.connect((ip, 10000))

def recvinfor():
    print("连接成功！现在可以接收消息！")
    while True:
        try:
            # 测试发现，当服务器率先关闭时，这边也会报ConnectionResetError
            respon = s.recv(1024)
            print(respon.decode("gbk"))
        except ConnectionResetError:
            print("聊天结束！")
            s.close()
            break
    os._exit(0)


def sendinfor():
    print("连接成功！现在可以发送消息！")
    print("输入stop来退出聊天")
    while True:
        msg = input()
        if msg == "stop":
            print("你退出了聊天")
            s.close()
            break
        s.send(msg.encode("gbk"))
    os._exit(0)

threads = [threading.Thread(target=recvinfor), threading.Thread(target=sendinfor)]
for c in threads:
    c.start()