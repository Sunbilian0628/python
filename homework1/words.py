# -*- encoding: utf-8 -*-
'''
@File : 05.py
@Time : 2020/03/08 00:41:04
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
#!/usr/bin/python3

# 10 给定一段英文文本，统计每个单词出现的次数；
# 打印输出，按照词频从高到低输出：
# 提示：可以用字典来统计：key是单词，value是单词出现次数；
# 先创建一个字典，然后遍历刚刚取出的单词列表，接着做一个判断： 
# 如果字典中key已经出现了这个单词，那么它对应的value,也就是出现次数就 +1
# 如果这个单词没出现过，就直接插入这个单词及value为1到字典中

dict1={}
list1=[
    'my',
    'name',
    'is',
    'name',
    'random',
    'my',
    'Lisa',
    'my'
]
for i in list1:
    if i in dict1:
        dict1[i]=dict1[i]+1
    else:
        dict1[i]=1
dict2=sorted(dict1.items(),key=lambda x: x[1],reverse=True)
print(dict2)