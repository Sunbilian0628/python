# 3  设计一个留言本的表（ID，留言内容，留言人，留言时间，是否删除）
# （表名，和字段名自己设计成英文：注意，不要用中文，用中文的直接0分）；
#  使用sqlalchemy 驱动模块，实现对这个表的增加，删除，修改，查询；
#  数据库操作需要加入异常处理逻辑；

# 导入:
from sqlalchemy import Column, String, create_engine, Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类:
Base = declarative_base()


# 创建一个表的元素的类，方便之后构造对象:
class User(Base):
    # 表的名字:
    __tablename__ = 'messages'

    # 表的结构:
    ID = Column(Integer, primary_key=True, nullable=False)
    content = Column(String(20))
    member = Column(String(20))
    writime = Column(String(20))
    is_del = Column(Integer)


# 初始化数据库连接:
engine = create_engine('mysql+mysqlconnector://root:123456@127.0.0.1:3306/messagetext')


# 增加
def appli():
    # 创建DBSession类型:
    DBSession = sessionmaker(bind=engine)
    # 创建session对象:
    session = DBSession()
    # 创建新对象:
    u1 = User(ID='6', content='no', member='Bob', writime='20190526', is_del=0)
    try:
        # 添加到session:
        session.add(u1)
        # 提交即保存到数据库:
        session.commit()
        # 关闭session:
    except Exception as e:
        print('添加异常')
    session.close()


def dele():
    # 创建DBSession类型:
    DBSession = sessionmaker(bind=engine)
    # 创建Session:
    session = DBSession()
    try:
        # 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
        user = session.query(User).filter(User.ID == '3').delete()
        # 提交即保存到数据库:
        session.commit()
    except Exception as e:
        print('删除异常')
    # 关闭Session:
    session.close()


def change():
    # 创建DBSession类型:
    DBSession = sessionmaker(bind=engine)
    # 创建Session:
    session = DBSession()
    try:
        # 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
        user = session.query(User).filter(User.ID == '2').update({'content': 'my god'})
        # 提交即保存到数据库:
        session.commit()
    except Exception as e:
        print('修改异常')
    # 关闭Session:
    session.close()


def sear():
    # 创建DBSession类型:
    DBSession = sessionmaker(bind=engine)
    # 创建Session:
    session = DBSession()
    try:
        # 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
        user = session.query(User).filter(User.ID == '4').one()
        # 打印
        print('ID:', user.ID)
        print('content:', user.content)
        print('member:', user.member)
        print('writime:', user.writime)
        print('is_del:', user.is_del)
    except Exception as e:
        print('查询异常')
    # 关闭Session:
    session.close()


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
    # 打印
    for i in user:
        print('ID:{0}, content:{1}, member:{2}, writime:{3}, is_del:{4}'
              .format(i.ID, i.content, i.member, i.writime, i.is_del))
    # 关闭Session:
    session.close()


if __name__ == "__main__":
    appli()
    print('---------------------------')
    print('添加后的数据为')
    pri()
    dele()
    print('---------------------------')
    print('删除后的数据为')
    pri()
    change()
    print('---------------------------')
    print('修改后的数据为')
    pri()
    print('---------------------------')
    print('查找的数据为')
    sear()
