# -*- encoding: utf-8 -*-
'''
@File : 03.py
@Time : 2020/04/22 13:01:51
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

# 3  给定一个网址（包含了优质的英语学习音频文件），
# http://www.listeningexpress.com/studioclassroom/ad/；  
# 请大家写一个爬虫，将里面的英语节目MP3，都下载下来；
# 这些音频文件 在网页的html文件内容都是以mp3结尾的，如下图所示：
# 要求大家使用Requests库获取这个网页html文本内容，
# 并且使用正则表达式获取里面所有的mp3文件的网址；并进行下载；
# Windows上的wget可以点击这里 下载。 这个程序不用安装，直接在命令行里使用即可；
# 注意：
# 获取的音频网址前面需要加上 前缀 
# http://www.listeningexpress.com/studioclassroom/ad/ 才是完整的下载地址
# MP3文件中有空格字符，组成下载网址时，需要进行url编码，
# 否则空格会被当成命令行分隔符。参考代码如下所示
# >>> from urllib.parse import quote
# >>> quote('2019-04-13 NEWSworthy Clips.mp3')
# '2019-04-13%20NEWSworthy%20Clips.mp3'

import wget
import re
import requests
from urllib.parse import quote
import os


def getURL(url):
    try:
        list1 = []
        headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36"}
        r = requests.get(url, headers = headers)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        text = r.text
        a = re.findall(r'sc-ad [-\'\s\w\d]*\.mp3', text)
        for i in range(0,len(a)):
            a[i] = a[i][6:-1]
            list1.append(a[i])
        return list1
    except:
        print('爬取失败！')

def down(url):
    for i in url:
        j = quote(str(i))
        k = "http://www.listeningexpress.com/studioclassroom/ad/"
        wget.download(k,j)
        print('{}文件下载完成'.format(j))

if __name__ == "__main__":
    url = "http://www.listeningexpress.com/studioclassroom/ad/"
    a = getURL(url)
    down(a)