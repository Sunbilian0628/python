# -*- encoding: utf-8 -*-
'''
@File : _student.py
@Time : 2020/04/11 22:46:09
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

# 二 定义一个学生Student类。有下面的类属性：
# 1 姓名 name
# 2 年龄 age
# 3 成绩 score（语文，数学，英语) [每课成绩的类型为整数]
# 类方法：
# 1 获取学生的姓名：get_name() 返回类型:str
# 2 获取学生的年龄：get_age() 返回类型:int
# 3 返回3门科目中最高的分数。get_course() 返回类型:int
# 写好类以后，可以定义2个同学测试下:

class student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
    def get_course(self):
        list.sort(self.score, reverse=True)
        print("3门科目中最高的分数是{}分".format(self.score[0]))
        return self.score[0]

list1 = [81, 94, 96]
a = student('张三', 17, list1)
print('学生姓名为：{}'.format(a.get_name()))
print('学生年龄为：{}'.format(a.get_age()))
a.get_course()

list2 = [89, 74, 90]
b = student('李四', 18, list2)
print('学生姓名为：{}'.format(b.get_name()))
print('学生年龄为：{}'.format(b.get_age()))
b.get_course()