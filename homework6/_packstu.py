# -*- encoding: utf-8 -*-
'''
@File : _packstu.py
@Time : 2020/04/11 22:47:48
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

# 四 .封装一个学生类，有姓名，有年龄，有性别，有英语成绩，数学成绩，语文成绩，
#       封装方法，求单个学生的总分，平均分，以及打印学生的信息。

class student(object):
    def __init__(self, name, age, sex, Engilsh, math, Chinese):
        self.name = name
        self.age = age
        self.sex = sex
        self.Engilsh = Engilsh
        self.math = math
        self.Chinese = Chinese
    def _sum(self):
        return self.Engilsh + self.math + self.Chinese
    def aver(self):
        sum = self.Engilsh + self.math + self.Chinese
        ave = sum/3
        sum = ("%.3f" %ave)
        return sum
    def printf(self):
        print("姓名:{}".format(self.name))
        print("年龄:{}".format(self.age))
        print("性别:{}".format(self.sex))
        print("英语成绩:{}".format(self.Engilsh))
        print("数学成绩:{}".format(self.math))
        print("语文成绩:{}".format(self.Chinese))
        print("总成绩:{}".format(self._sum()))
        print("平均成绩:{}".format(self.aver()))

a = student('张三', 18, '男', 88, 90, 85)
print("总成绩为:{}".format(a._sum()))
print("平均成绩为:{}".format(a.aver()))
a.printf()