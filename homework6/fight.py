# -*- encoding: utf-8 -*-
'''
@File : fight.py
@Time : 2020/04/11 22:50:05
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

# 五  请写一个小游戏，人狗大站;  规则:
#     1   2个角色，人和狗，游戏开始后，生成2个人，3条狗，
#     人狗互相交替对战(注意,人只能打狗,  狗也只会咬人); 
#     人的打击力为10;  初始化血为100;    狗的攻击力为 15; 初始化血为80;
#     2  人被狗咬了会掉血，狗被人打了也掉血，
#     狗和人的攻击力，具备的功能都不一样。血为0的话,表示死亡,退出游戏;
#     人和狗的攻击力,都会因为被咬, 或者被打而降低
#     (人被咬一次,打击力降低2; 狗被打一次,攻击力降低3);
#     3   对战规则: 
#      A  随机决定,谁先开始攻击; 
#      B  一方攻击完毕后, 另外一方再开始攻击; 
#      攻击的目标是随机的(比如, 人要打狗了, 随机找一条血不为0的狗攻击);
#      C  每次攻击, 双方只能安排一个人,或者一条狗进行攻击;
# 提示：注意组织代码的方式；狗类用一个单独的py文件； 人用一个单独的py文件； 
# 在写一个fight模块（也用类来组织；在这个模块中，导入人和狗模块中编写好的方法）


from _dog import dog
from _people import people
import random

class fight(object):
    def start(self):
        p1 = people('people1')
        p2 = people('people2')
        d1 = dog('dog1')
        d2 = dog('dog2')
        d3 = dog('dog3')
        list1 = []
        list1.append(p1)
        list1.append(p2)
        list2 = []
        list2.append(d1)
        list2.append(d2)
        list2.append(d3)
        i = random.choice(range(0,1))
        if i == 0:
            while True:
                d1.attack(list2, list1)
                p1.attack(list1, list2)
                if len(list1) == 0:
                    print("人输了")
                    return
                if len(list2) == 0:
                    print("狗输了")
                    return
        else:
            while True:
                p1.attack(list1, list2)
                d1.attack(list2, list1)
                if len(list1) == 0:
                    print("人输了")
                    return
                if len(list2) == 0:
                    print("狗输了")
                    return

f = fight()
f.start()