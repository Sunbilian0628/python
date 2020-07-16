# 给定10万个企业的网址(放在数据库表中),请编写一个网络爬虫
# 爬取该企业的产品及服务信息(即获取该企业能提供的产品和服务)
# 并将爬取到的数据,保存到数据库中,请自行设计数据库表结构

# 步骤
# 1.数据库连接提取网址
# 2.爬虫爬取数据
# 3.保存到数据库
# 4.多线程或者多进程实现（由于电脑配置问题推荐多线程，线程池）

# 本主程序涉及的其他程序部分已经分拆到了其他文件夹中
# 方便日后对特定部分文件的修改
# 另外爬虫部分有待完善
# 日后进行修改时可以进行进一步完善

from concurrent.futures import ThreadPoolExecutor
from sqlalchemy import Column, String, create_engine, Integer, Text, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import requests
from bs4 import BeautifulSoup

# 连接数据库
# 创建对象的基类:
Base = declarative_base()

# 创建一个表的元素的类，方便之后构造对象:
class User(Base):
    # 表的名字:
    __tablename__ = 'company'

    # 表的结构:
    autoID = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    enterpriseID = Column(String(32))
    entid = Column(Integer)
    enterpriseName = Column(String(255))
    web_url = Column(Text)
    addtime = Column(TIMESTAMP)


# 初始化数据库连接:
engine = create_engine('mysql+mysqlconnector://root:123456@127.0.0.1:3306/work11')


# 创建一个表的元素的类，方便之后构造对象:
class Users(Base):
    # 表的名字:
    __tablename__ = 'infor'

    # 表的结构:
    ID = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(64))
    content = Column(Text)
    web_url = Column(String(200))

# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)
# 创建session对象:
session = DBSession()
Base.metadata.create_all(engine)
session.commit()

# 增加
def appli(Name, Content, Web_url):
    # 创建DBSession类型:
    DBSession = sessionmaker(bind=engine)
    # 创建session对象:
    session = DBSession()
    # 创建新对象:
    u1 = Users(name=Name, content=Content, web_url=Web_url)
    print(u1.content)
    try:
        # 添加到session:
        session.add(u1)
        # 提交即保存到数据库:
        session.commit()
        # 关闭session:
    except Exception as e:
        print('添加异常')
    session.close()

# 提取数据
def pri():

    # 创建DBSession类型:
    DBSession = sessionmaker(bind=engine)
    # 创建Session:
    session = DBSession()
    try:
        # 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
        user = session.query(User).all()
    except Exception as e:
        print('查询异常')
    # 关闭Session:
    session.close()
    return user



def getinfor(i):
    list1 = [
        '产品',
        '服务信息',
        '主要产品',
        '客户服务',
        '新书速递',
        '疑难业务处理'
        '业务',
        '热点产品',
        '查询服务',
        '业务领域',
        '业务领域',
        '重点业务',
        '业务介绍',
        '全部产品',
        '业务领域',
        '品牌产品',
        '产品中心',
        '服务中心',
        '业务与产品',
        '公司产品',
        '产业板块',
        'Our Business',
        '服务专区',
        '业务板块',
        '数字产品',
        '服务互动',
        '展会品牌'
    ]
    user = pri()
    url = user[i].web_url.replace(" ", "")
    u = url.split(';')
    print(u[0])
    list2 = getall(u[0], list1)
    list3 = str(list2)
    appli(user[i].enterpriseName, list3, url)

# 爬虫部分

def getall(url, list1):
    try:
        headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36"}
        r = requests.get(url, headers=headers, timeout=1)
    except:
        list2 = '网址无法打开'
        print('连接失败')
        return list2
    else:
        r.encoding = r.apparent_encoding
        text = r.text
        soup = BeautifulSoup(text, "html.parser")
        list3 = []

        # ***************************************************************
        # 一层爬虫，爬取第一种方法能索引到的有效数据
        # ***************************************************************

        for i in list1:
            div_items = soup.find(text=i)
            if div_items == None:
                continue
            next_siblings = div_items.find_all_next('ul')
            if len(next_siblings) > 0:
                next_str = next_siblings[0]
            else:
                break
            for k in next_str.find_all('a'):
                list3.append(k.string)
        list2 = list(set(list3))
        if list2 != []:
            list5 = ' '.join(str(x) for x in list2)

        # ***************************************************************
        # 如果在一层爬虫中未索引到数据则进入二层爬虫
        # ***************************************************************

        if list2 == []:
            a = soup.select("a")
            for i in a:
                if i.string in list1:
                    htp = i['href']
                    http = url + '/' + str(htp)
                    try:
                        r1 = requests.get(http, headers=headers, timeout=5)
                    except:
                        l = '网址无法打开'
                        print('连接失败')
                        return l
                    else:
                        r1.encoding = r1.apparent_encoding
                        t = r1.text
                        s = BeautifulSoup(t, "html.parser")
                        a1 = s.find_all('h3')
                        list2.append(i.string)
                        for k in a1:
                            print(k.string+' ', end='')
                            list2.append(k.string)
                    list1.remove(i.string)
            list2 = list(set(list2))
            if list2 != []:
                list5 = ' '.join(str(x) for x in list2)

        # ***************************************************************
        # 二层索引也未索引到数据则进入三层索引中
        # ***************************************************************

        if list2 == []:
            list5 = ''
            title = soup.select("title")
            if title != None:
                list2 = list(set(title))
                if len(list2) > 0:
                    list5 = str(list2[0].string)
                    list5.replace(' ', '')
            head = soup.a
            if head != None:
                list3 = list(head)
                if len(list3) > 0:
                    x = str(list3[0].string)
                    x.replace(' ', '')
                    if list5 != '':
                        list5 = list5 + ' ' + x
                    else:
                        list5 = x
        if list2 == []:
            a = '网页内无相关信息'
            return a
        return list5

# 多线程

def build():
    list1 = [x for x in range(0, 100000)]
    return list1

def func(list1):
    for i in range(1000):
        a = list1.pop(i)
        getinfor(a)



if __name__ == "__main__":
    list1 = build()
    pool = ThreadPoolExecutor(100)
    for i in range(0, 100):
        task = pool.submit(func(list1))