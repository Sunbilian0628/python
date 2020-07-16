# -*- encoding: utf-8 -*-
'''
@File : 02.py
@Time : 2020/04/26 00:19:58
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

# 2 给定一组数据网址数据，请判断这些网址是否可以访问； 用多线程的方式来实现；
#    请查资料，Python的 requests库，如何判断一个网址可以访问；
# 提示 ：使用requests模块
#    def getHtmlText(url):
#     try:        # 网络连接有风险，异常处理很重要
#         r = requests.get(url,timeout=30)    # 查一下这个方法的使用
#         r.raise_for_status()       # 如果状态不是200，引发HTTPError异常
#         r.encoding = r.apparent_encoding
#         return r.text
#     except:
#          return "产生异常"
#   数据文件（1000个网址）

import requests


def getHtmlText(url):
    try:
        r = requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        with open("homework8//url_cun.txt", 'w') as f:
            f.write(r.text)
    except Exception:
        print("{}产生异常".format(url))

def geturl():
    with open("homework8//url_data.txt", 'r') as f:
        lines = f.readlines()
    for i in lines:
        getHtmlText(i.strip())

if __name__ == "__main__":
    geturl()