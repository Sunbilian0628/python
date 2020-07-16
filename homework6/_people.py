# -*- encoding: utf-8 -*-
'''
@File : _people.py
@Time : 2020/04/11 22:50:01
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

import random

class people(object):
    power = 10
    blood = 100
    #狗打人
    def __init__(self, name):
        self.name = name
    def attack(self, list1, list2):
        if len(list1) == 0:
                return
        if len(list2) == 0:
                return
        i = random.choice(list1)
        j = random.choice(list2)
        print("{}攻击{}".format(j.name,i.name))
        i.blood = i.blood-10
        print("{}减10点血".format(i.name))
        i.power = i.power-3
        print("{}减3点攻击力".format(i.name))
        if i.blood <= 0:
            list1.remove(i)
            print("{}死亡".format(i.name))