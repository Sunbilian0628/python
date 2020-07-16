# -*- encoding: utf-8 -*-
'''
@File : server.py
@Time : 2020/05/05 21:57:44
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
#!/usr/bin/python3
# 3 编写一个UDP的聊天程序，客户端和服务器端能互相聊天应答；

# 服务器

import socket
import sys

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

host = socket.gethostname()
port = 9999

# 绑定端口号
server.bind((host, port))

# 设置最大连接数，超过后排队
server.listen(5)

# 服务器一直循环等待
while True:
    # 接收客户端连接
    client,addr = server.accept()
    # 输出链接地址 
    print("连接地址: %s" % str(addr))
    # 在客户端出输出欢迎语句
    msg='欢迎访问菜鸟教程！'+ "\r\n"
    client.send(msg.encode('utf-8'))
    client.close()