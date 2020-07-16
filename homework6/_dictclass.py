# -*- encoding: utf-8 -*-
'''
@File : _dictclass.py
@Time : 2020/04/11 22:46:57
@Author : xdbcb8 
@Version : 1.0
@Contact : 2996778429@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

# 三、定义一个字典类：dictclass。完成下面的功能：
# dict = dictclass({你需要操作的字典对象})
# 1 删除某个key
# del_dict(key)
# 2 判断某个键是否在字典里，如果在返回键对应的值，不存在则返回"not found"
# get_dict(key)
# 3 返回键组成的列表：返回类型;(list)
# get_key()
# 4 合并字典，并且返回合并后字典的values组成的列表。返回类型:(list)
# update_dict({要合并的字典})

class dictclass(object):
    def __init__(self, dict1):
        self.dict1 = dict1
    def del_dict(self, key):
        if key in self.dict1:
            del self.dict1[key]
            print('已删除')
        else:
            print('未找到要删除的key值')
    def get_dict(self, key):
        if key in self.dict1:
            return self.dict1[key]
        else:
            print('not found')
    def get_key(self):
        list1 = self.dict1.keys()
        return list1
    def update_dict(self, dict2):
        self.dict1.update(dict2)
        list2 = self.dict1.values()
        return list2

dict1 = {'a': 10, 'b': 8, 'c': 4}
a = dictclass(dict1)
a.del_dict('a')
print('键是否在字典里（如果在返回键对应的值）:')
print(a.get_dict('b'))
print('键组成的列表：')
print(list(a.get_key()))
print('合并后字典的values组成的列表:')
dict2 = {'d': 6, 'e': 9}
print(list(a.update_dict(dict2)))