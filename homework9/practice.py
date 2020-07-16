# -*- encoding: utf-8 -*-
'''
@File : 01.py
@Time : 2020/04/30 14:38:12
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
# 1 将“网络编程”章节中课件中的例子，在本机测试运行；下载安装网络编程调试工具

# import socket

# 创建tcp的套接字
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 不用的时候，关闭套接字
# s.close()

# 创建一个udp socket（udp套接字）
# import socket

# 创建udp的套接字
# s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 不用的时候，关闭套接字
# s.close()


# import socket

# def main1():
#     #1 创建一个udp套接字
#     udp_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    
#     # 2. 准备接收方的地址 使用udp套接字发送数据:发什么,发给谁
#     # '192.168.1.24'表示目的ip地址
#     # 8888表示目的端口
#     dest_addr = ('192.168.1.103', 8888)  # 注意 是元组，ip是字符串，端口是数字

#     # 3. 从键盘获取数据
#     send_data = input("请输入要发送的数据:")
#     # 4. 发送数据到指定的电脑上的指定程序中
#     udp_socket.sendto(send_data.encode('utf-8'), dest_addr)
    
#     # 5 关闭套接字
#     udp_socket.close()


# UDP 接收网络数据

# def main2():
#    # 绑定端口信息
#     udp_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    
#     local_addr=('',9999)

#     udp_socket.bind(local_addr)
#    # 接收数据
#     recv_data = udp_socket.recvfrom(1024)  # 1024表示本次接收的最大字节数
#    # 打印显示接收到的数据
#     print(recv_data)

#     print(recv_data[0].decode('gbk'))
#     print(recv_data[1])

#    # 关闭套接字
#     udp_socket.close()

# if __name__ == "__main__":
#     # main1()
#     main2()



#!/usr/bin/python3
# 文件名：client.py

# 导入 socket、sys 模块
# import socket
# import sys

# # 创建 socket 对象
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

# # 获取本地主机名
# host = socket.gethostname() 

# # 设置端口号
# port = 9999

# # 连接服务，指定主机和端口
# s.connect((host, port))

# # 接收小于 1024 字节的数据
# msg = s.recv(1024)

# s.close()

# print (msg.decode('utf-8'))