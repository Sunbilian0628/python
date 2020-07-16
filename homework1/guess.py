# -*- encoding: utf-8 -*-
'''
@File : 04.py
@Time : 2020/03/08 01:38:20
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
#!/usr/bin/python3

# 9 设计一个猜数字 游戏
# 最多只能猜测N次，在N次之内猜不出，就退出程序，提示猜测失败


m = 6 #谜底
n = 5 #猜测次数
flag = 0
print("猜数字游戏!")
number = 0
while m != number:
    number=int(input("请输入您猜的数字："))
    flag=flag+1
    if flag >= n:
        print("游戏失败！")
        break
    if number == m:
        print("恭喜，你猜对了！")
    elif number < m:
        print("猜的数字小了...")
    elif number > m:
        print("猜的数字大了...")