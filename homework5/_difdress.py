# -*- encoding: utf-8 -*-
'''
@File : 04.py
@Time : 2020/04/06 20:30:44
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib


# 4  编写装饰器来实现，对目标函数进行装饰，
# 分3种情况：目标函数无参数无返回值，目标函数有参数，目标函数有返回值；
#      三个目标函数分别为：
#      A 打印输出20000之内的素数；
#      B 计算整数2-10000之间的素数的个数；
#      C 计算整数2-M之间的素数的个数；
#   可以观看给的视频材料，仿照示例来做


# 目标函数无参数无返回值
# A 打印输出20000之内的素数

# def _applica(func):
#     def datext():
#         print('素数有：')
#         func()
#     return datext

# @_applica
# def _sunumber():
#     for i in range(2, 20000):
#         for j in range(2,i):
#             if i%j == 0:
#                 break
#         else:
#             print(i)

# _sunumber()


# 目标函数有返回值
# B 计算整数2-10000之间的素数的个数

# def _applicas(func):
#     def datexts():
#         print('素数有：',end = '')
#         res = func()
#         print('{}个'.format(res))
#     return datexts

# @_applicas
# def _sunumbers():
#     count = 0
#     for i in range(2, 10000):
#         for j in range(2,i):
#             if i%j == 0:
#                 break
#         else:
#             count = count + 1
#     return count

# _sunumbers()


# 目标函数有参数
# C 计算整数2-M之间的素数的个数；

def _applicat(func):
    def datextt(a):
        print('2-M之间的素数的个数有：',end = '')
        res = func(a)
        print('{}个'.format(res))
    return datextt

@_applicat
def _sunumbert(a):
    count = 0
    for i in range(2, a):
        for j in range(2,i):
            if i%j == 0:
                break
        else:
            count = count + 1
    return count

a = int(input('请输入M的值：'))
_sunumbert(a)