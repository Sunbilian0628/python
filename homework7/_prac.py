# -*- encoding: utf-8 -*-
'''
@File : 04.py
@Time : 2020/04/22 13:02:02
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

# 4 爬取这个网址上http://www.python3.vip/doc/prac/python/0001/，
# 所有的Python练习题题目和答案；保存到txt文件中（只保留文字）；
# 文本文件类似（注意是类似的效果，不是说一定要做的一模一样）

import re
import requests
from bs4 import BeautifulSoup
from urllib import error

def linkurl(url):
    try:
        headers = {	'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3724.8 Safari/537.36'}
        r = requests.get(url,headers=headers,timeout = 5).content.decode('utf-8')
    except error.URLError:
        print('{}连接失败'.format(url))
    else:
        t = BeautifulSoup(r,'html.parser')
        a = t.find_all('div', {'class', 'content'})
        text = a[0].find_all(['code','p','h2','span'])
        for i in text:
            if i.string !=None:
                # print(i.string)
                with open('homework7\\practice.txt','a+',encoding='utf-8') as f:
                    f.write(i.string+'\n')
                    f.write('\n')
        with open('homework7\\practice.txt','a+',encoding='utf-8') as f1:
            f1.write('*'*50+'\n')

def getweb():
    dict = {}
    url = 'http://www.python3.vip/doc/prac/python/0001/'
    headers = {	'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3724.8 Safari/537.36'}
    r = requests.get(url,headers=headers).content.decode('utf-8')
    # obj=re.findall(r'<a herf="http://www.python3.vip/doc/prac/python/[a-zA-Z0-9\.-\u4e00-\u9fa5]+\.[com|cn|org|net]*',r)
    t = BeautifulSoup(r,'html.parser')
    a = t.find_all('', {'class', 'nav__items'})
    # print(a)
    text = a[0].find_all('a')
    # print(text)
    for i in text:
        if i.string !=None and i.string!='自定义类':
            if i.attrs['href'] !=None:
                dict[i.string] = i.attrs['href']
    for j, k in dict.items():
        with open('homework7\\practice.txt','a+',encoding='utf-8') as f:
            f.write('*'*50+'\n')
            f.write(j+'\n')
            linkurl(str(k))
    

getweb()