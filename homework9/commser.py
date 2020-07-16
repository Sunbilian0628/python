# -*- encoding: utf-8 -*-
'''
@File : 04.py
@Time : 2020/04/30 14:38:31
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
# 4 设计一款能实现多人聊天的系统：使用socket和多线程技术，编写全多人聊天室

# 服务器

import socket
import threading
import os

def getip():
    # 获得本机地址
    host = socket.gethostname()
    # 根据主机名获取IP地址，并返回数据
    ip = socket.gethostbyname(host)
    return ip

# 服务器类
class sever:
    # 初始化
    def __init__(self):
        # 地址链接
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 端口链接本机
        self.dizhi = (getip(), 10000)
        # 记录当前用户个数
        self.users = {}
    
    # 绑定主机接收端，接收客户端
    def startsev(self):
        self.sock.bind(self.dizhi)
        self.sock.listen(5)
        print("服务器已开启，等待连接...")
        print("输入stop可关闭服务器")
        # 死循环接收客户端端口
        self.acceptse()
    
    # 使用多线程接收各个用户
    def acceptse(self):
        while True:
            # 链接客户端
            s, addr = self.sock.accept()
            self.users[addr] = s
            # 当有用户链接进来时输出现有人数
            number = len(self.users)
            print("用户{}连接成功！现在共有{}位用户".format(addr, number))
            # 多线程
            threading.Thread(target=self.recve, args=(s, addr)).start()
            
    def recve(self, sock, addr):
        while True:
            try:  
                # 测试后发现，当用户率先选择退出时，这边就会报ConnectionResetError
                response = sock.recv(1024).decode("gbk")
                msg = "用户{}发来消息：{}".format(addr, response)
                # 输出消息
                print(msg)
                for c in self.users.values():
                    c.send(msg.encode("gbk"))
            except ConnectionResetError:
                print("用户{}已经退出聊天！".format(addr))
                self.users.pop(addr)
                break

if __name__ == "__main__":
    seve = sever()
    seve.startsev()