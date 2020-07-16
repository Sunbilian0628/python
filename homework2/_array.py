# -*- encoding: utf-8 -*-
'''
@File : ww.py
@Time : 2020/03/08 18:32:16
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
#!/usr/bin/python3

# 9  定义一个函数，函数接收一个数组，
# 并把数组里面的数据从小到大排序(冒泡排序,  也可以直接使用相关的函数);

def array(l):
    return sorted(l)

list1=eval(input("请输入数组："))
print("结果为：{}".format(array(list1)))