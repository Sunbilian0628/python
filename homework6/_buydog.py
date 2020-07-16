# -*- encoding: utf-8 -*-
'''
@File : _dog.py
@Time : 2020/04/11 22:45:19
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

# 一、定义一个狗类,里面有一个 列表成员变量(列表的元素是字典), 
# 分别记录了 3种颜色的狗的颜色, 数量,和价格;
# 实现狗的买卖交易方法;  打印输出经过2-3次买卖方法后,剩下的各类狗的数量;

class dog:
    list1 = [
        {'color' : '棕色', 'count' : 5, 'price' : 200},
        {'color' : '白色', 'count' : 3, 'price' : 350},
        {'color' : '黑色', 'count' : 2, 'price' : 250}
    ]
    def sell(self, color, number):
        for i in self.list1:
            if i['color'] == color:
                print("申请购买{}的狗{}只".format(color, number))
                if i['count'] - number > 0:
                    i['count'] = i['count'] - number
                    print("请支付{}元".format(i['price']*number))
                    print("购买完成")
    def buy(self, color, number):
        for i in self.list1:
            if i['color'] == color:
                i['count'] = i['count'] + number
                print("买入{}的狗{}只".format(color, number))
    def printf(self):
        for i in self.list1:
            print("颜色：{},数量:{},单价:{}".format(i['color'],i['count'],i['price']))

a = dog()
a.printf()
a.buy('棕色',2)
a.printf()
b = dog()
b.sell('白色',1)
b.printf()