# 2  设计一个留言本的表（ID，留言内容，留言人，留言时间，是否删除）
# （表名，和字段名自己设计成英文：注意，不要用中文，用中文的直接0分）；
#  使用PyMySQL 驱动模块，实现对这个表的增加，删除，修改，查询；
#  数据库操作需要加入异常处理逻辑；

import pymysql

# 增加
def appli():
    # 打开数据库连接
    db = pymysql.connect(host="localhost", user="root", password="123456", db="messagetext")

    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    # SQL 插入语句
    sql = """INSERT INTO message(content, member, writime, is_del) 
                 VALUES ('world', 'Mary', '20191212', 1), ('i am fine', 'Lisa', '20200513', 0)"""
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
    except Exception as e:
        # 如果发生错误则回滚
        db.rollback()

    # 关闭数据库连接
    db.close()

# 遍历
def pri():
    # 打开数据库连接
    db = pymysql.connect(host="localhost", user="root", password="123456", db="messagetext")

    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    # SQL 查询语句
    sql = "SELECT * FROM message "
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        result = cursor.fetchall()
        for i in result:
            print("ID = '%s', content = '%s', member = '%s', writime = '%s', is_del = '%s'" %
                  (i[0], i[1], i[2], i[3], i[4]))
    except Exception as e:
        print("Error: unable to fetch data")

# 删除
def dele():
    # 打开数据库连接
    db = pymysql.connect(host="localhost", user="root", password="123456", db="messagetext")

    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    # SQL 删除语句
    sql = "DELETE FROM message WHERE ID = %s" % (4)
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 提交修改
        db.commit()
    except Exception as e:
        # 发生错误时回滚
        db.rollback()

    # 关闭连接
    db.close()

# 修改
def change():
    # 打开数据库连接
    db = pymysql.connect(host="localhost", user="root", password="123456", db="messagetext")

    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    # SQL 更新语句
    sql = "UPDATE message SET content = '%s' WHERE id = '%s'" % ('hi everybody', 1)
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
    except Exception as e:
        # 发生错误时回滚
        db.rollback()

    # 关闭数据库连接
    db.close()

# 查询
def search():
    # 打开数据库连接
    db = pymysql.connect(host="localhost", user="root", password="123456", db="messagetext")

    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    # SQL 查询语句
    sql = "SELECT * FROM message WHERE ID = '%s'" % (2)
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        for i in results:
            # 打印结果
            print("ID = '%s', content = '%s', member = '%s', writime = '%s', is_del = '%s'" %
                  (i[0], i[1], i[2], i[3], i[4]))
    except Exception as e:
        print("Error: unable to fetch data")

if __name__ =="__main__":
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
    search()