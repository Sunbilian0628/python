# -*- encoding: utf-8 -*-
'''
@File : work2.py
@Time : 2020/03/05 23:02:24
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
#!/usr/bin/python3

# 2 一个字典中，存放了10个学生的学号（key）和分数（value）；
# 请筛选输出，大于80分的同学（按照格式：学号：分数）

dict1={
    12018100:97,
    12018101:80,
    12018102:75,
    12018103:77,
    12018104:78,
    12018105:65,
    12018106:66,
    12018107:88,
    12018108:89,
    12018109:95
}
for k,v in dict1.items():
    if v>80:
        print(k,v)