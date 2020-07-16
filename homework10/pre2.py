# 练习二：
#    创建一个留言板的表（ID，留言主题，留言人，留言时间）4个字段，注意，字段请用英文；
#    完成对这个表记录的增，删，改，查询；
#    用PyMySQL驱动方式

# !/usr/bin/python3

import pymysql

# 创建表
def crebiao():

    # 打开数据库连接
    db = pymysql.connect(host="localhost", user="root", password="123456", db="test")

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()

    # 使用预处理语句创建表
    sql = """CREATE TABLE message (
             ID INT primary key AUTO_INCREMENT  NOT NULL,
             item  CHAR(20),
             person CHAR(20),  
             time CHAR(20)
             )"""
    try:
        cursor.execute(sql)

    except:
        # 如果发生错误则回滚
        db.rollback()

    # 关闭数据库连接
    db.close()

# 增加
def addition():
    # 打开数据库连接
    db = pymysql.connect(host="localhost", user="root", password="123456", db="test")

    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    # SQL 插入语句
    sql = """INSERT INTO message(
             item, person, time)
             VALUES ('hello', 'Tom', '8:00'), ('world', 'Lisa', '9:00'), ('hi', 'Cindy', '9:00')"""
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
    except:
        # 如果发生错误则回滚
        db.rollback()

    # 关闭数据库连接
    db.close()
def dele():
    engj

def printf():
    # 打开数据库连接
    db = pymysql.connect(host="localhost", user="root", password="123456", db="test")

    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    # SQL 查询语句
    sql = "SELECT * FROM message "
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        for i in results:
            # 打印结果
            print("ID='%s', item='%s', person='%s', time='%s'" % \
                  (i[0], i[1], i[2], i[3]))
    except:
        print("Error: unable to fetch data")

if __name__ == '__main__':
    crebiao()
    addition()
    print('---------------------------')
    print('添加后的数据为')
    printf()
    dele()
    print('---------------------------')
    print('删除后的数据为')
    printf()
    change()
    print('---------------------------')
    print('修改后的数据为')
    printf()
    print('---------------------------')
    print('查找的数据为')
    search()