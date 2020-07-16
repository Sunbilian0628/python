# -*- encoding: utf-8 -*-
'''
@File : 02.py
@Time : 2020/04/19 23:41:13
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

# 2 给定100个企业网站首页链接地址（用1中给出的URL地址）；
# 请爬取每个页面上，企业介绍的链接地址；
#     说明，满足企业介绍网址的条件是， 标题包含：
#     企业介绍，关于我们，企业发展，发展历史，企业概况等关键字的URL地址；
#     提示：要用到requests库，BeautifulSoup库


import requests
from bs4 import BeautifulSoup
import os, re
import time


def getall(url, list1):
    try:
        headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36"}
        r = requests.get(url, headers = headers, timeout = 5)
    except:
        print('{}连接失败'.format(url))
    else:
        r.encoding = r.apparent_encoding
        text = r.text
        soup = BeautifulSoup(text, "html.parser")
        a = soup.select("a")
        for i in a:
            if i.string in list1:
                htp = i['href']
                http = url+'/'+str(htp)
                print(i.string, http)
                with open("homework7//cunweb.txt", 'a', encoding='utf-8')as f:
                    f.write(i.string+' '+http+'\n')
                list1.remove(i.string)


def getinfor():
    # with open("homework7//web.txt", 'r', buffering=1, encoding='utf-8')as f1:
    #     line = f1.read()
    # title = re.findall(r'[\(\)\u4e00-\u9fa5]*[公司|出版社|代表处]',line)
    for i in range(0, 100):
        # print(title[i])
        # with open("homework7//cunweb.txt", 'w', encoding='utf-8')as f1:
        #         f1.write(title[i]+' ')
        list1 = [
            '企业介绍',
            '公司介绍',
            '关于我们',
            '企业发展',
            '公司发展',
            '发展历史',
            '企业概况'
            ]
        with open("homework7//hunweb.txt", 'r', buffering=1, encoding='utf-8')as f:
            line2 = f.readlines()
        url = line2[i].strip()
        print(url)
        getall(str(url), list1)


if __name__ == '__main__':
    getinfor()