# -*- encoding: utf-8 -*-
'''
@File : _grade.py
@Time : 2020/04/11 22:49:40
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

# 六  用面向对象,实现一个学生Python成绩管理系统;
#       学生的信息存储在文件中;学生信息的字段有(班级,学号,姓名, Python成绩)
#       实现对学生信息及成绩的增,删,改,查方法;

import os

class student(object):
    def app(self, clas, name, number, grade):
        with open('homework6\\student.txt', 'a', encoding='utf-8') as f:
            f.write('{} {} {} {}\n'.format(clas, name, number, grade))
        print('添加完成')
    def dele(self):
        list2 = []
        num = input('请输入要删除的学生的学号：')
        with open('homework6\\student.txt', 'r', encoding='utf-8') as f:
            lines = f.readlines()
            for i in lines:
                list1 = i.strip().split()
                if list1[1] != num:
                    list2.append(i)
        with open('homework6\\student.txt', 'w', encoding='utf-8') as f1:
            f1.writelines(list2)
        print('删除完成')
    def change(self):
        list2 = []
        num = input('请输入要修改的学生的学号：')
        with open('homework6\\student.txt', 'r', encoding='utf-8') as f:
            lines = f.readlines()
            for i in lines:
                list1 = i.strip().split()
                if list1[1] == num:
                    a1 = input('请输入要修改的学生的班级：')
                    a2 = input('请输入要修改的学生的姓名：')
                    a3 = input('请输入要修改的学生的Python成绩：')
                    str = ('{} {} {} {}\n'.format(a1,num,a2,a3))
                    list2.append(str)
                else:
                    list2.append(i)
        with open('homework6\\student.txt', 'w', encoding='utf-8') as f1:
            f1.writelines(list2)
        print('修改完成')
    def search(self):
        num = input('请输入要查找的学生的学号：')
        with open('homework6\\student.txt', 'r', encoding='utf-8') as f:
            lines = f.readlines()
            for i in lines:
                list1 = i.strip().split()
                if list1[1] == num:
                    print("该学生的信息为：")
                    print('班级：{}'.format(list1[0]))
                    print('学号：{}'.format(list1[1]))
                    print('姓名：{}'.format(list1[2]))
                    print('Python成绩：{}'.format(list1[3]))
                    return
        print('未找到')
    def printf(self):
        with open('homework6\\student.txt', 'r', encoding='utf-8') as f:
            lines = f.readlines()
            print('班级       学号   姓名 Python成绩')
            for i in lines:
                print(i.strip())

a = student()
a.app('计算1801班', 120186, '张晴', 93)
a.printf()
a.dele()
a.printf()
a.change()
a.printf()
a.search()

# 软件1801班 120181 张三 98
# 软件1801班 120182 李四 84
# 计算1801班 120183 王五 65
# 计算1801班 120184 赵六 75
# 软件1801班 120185 吴起 99