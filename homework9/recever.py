# -*- encoding: utf-8 -*-
'''
@File : 03.py
@Time : 2020/04/30 14:38:26
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
# 3 编写一个UDP的聊天程序，客户端和服务器端能互相聊天应答
#!/usr/bin/python3

# 客户端

import socket
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
host = socket.gethostname() 

# 设置端口号
port = 9999

# 连接服务，指定主机和端口
s.connect((host, port))

# 接收小于 1024 字节的数据
msg = s.recv(1024)

s.close()
# 输出欢迎语句
print (msg.decode('utf-8'))