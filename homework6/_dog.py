# -*- encoding: utf-8 -*-
'''
@File : _dog.py
@Time : 2020/04/11 22:49:56
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

import random

class dog(object):
    power = 15
    blood = 80
    #人打狗
    def __init__(self, name):
        self.name = name
    def attack(self, list1, list2):
        if len(list2) == 0:
                return
        if len(list1) == 0:
                return
        i = random.choice(list1)
        j = random.choice(list2)
        print("{}攻击{}".format(j.name,i.name))
        i.blood = i.blood-20
        print("{}减20点血".format(i.name))
        i.power = i.power-2
        print("{}减2点攻击力".format(i.name))
        if i.blood <= 0:
            list1.remove(i)
            print("{}死亡".format(i.name))