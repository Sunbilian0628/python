# -*- encoding: utf-8 -*-
'''
@File : 02.py
@Time : 2020/04/30 14:38:19
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
# 2 编写一个接收数据的网络程序，由“网络调试工具”发送数据，你的程序接收数据并打印输出

import socket

def main():
    udp=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    local_addr=('',9999)
    udp.bind(local_addr)
    # 接收数据
    recv = udp.recvfrom(1024)  
    # 1024表示本次接收的最大字节数
    # 打印显示接收到的数据
    print('传送的数据为：')
    print(recv[0])
    print('发送地址与端口号为：')
    print(recv[1])
    print()
    print(recv)
    # 关闭套接字
    udp.close()

if __name__ == "__main__":
    main()