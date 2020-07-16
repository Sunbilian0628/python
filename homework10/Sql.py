# 1 数据库查询练习：
#    针对我们给大家的2张表（学生表和班级表），做以下查询；
# （查询脚本放在一个文件中，创建一个SQL文件夹，放到这个里面，最有提交到代码仓库）
# ① 查询所有男生的姓名，年龄，所在班级名称；
# ② 查询所有查询编号小于4或没被删除的学生；
# ③ 查询姓黄并且“名”是一个字的学生；
# ④ 查询编号是1或3或8的学生
# ⑤ 查询编号为3至8的学生
# ⑥ 查询未删除男生信息，按年龄降序
# ⑦  查询女生的总数
# ⑧  查询学生的平均年龄
# ⑨ 分别统计性别为男/女的人年龄平均值
# ⑩ 按照性别来进行人员分组如下显示（group by + group_concat()）；
#         | 男     | 彭于晏,刘德华,周杰伦,程坤,郭靖                                 |
# 	| 女     | 小明,小月月,黄蓉,王祖贤,刘亦菲,静香,周杰                        |
# 	| 中性   | 金星                                                       |
# 	| 保密   | 凤姐                                                       |

import pymysql

# 查询所有男生的姓名，年龄，所在班级名称；
def first():
    # 打开数据库连接
    db = pymysql.connect(host="localhost", user="root", password="123456", db="test")

    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    # SQL 查询语句
    sql = "SELECT * FROM students \
               WHERE gender = '%s'" % ('男')
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        print('查询所有男生的姓名，年龄，所在班级名称为:')
        for i in results:
            # 打印结果
            print("name = '%s', age = '%s', cls_id = '%s'" % \
                  (i[1], i[2], i[5]))
    except:
        print("Error: unable to fetch data")

# 查询所有查询编号小于4或没被删除的学生；
def second():
    # 打开数据库连接
    db = pymysql.connect(host="localhost", user="root", password="123456", db="test")

    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    # SQL 查询语句
    sql = "SELECT * FROM students \
                   WHERE id < '%s' or is_delete = '%s'" % (4,0)
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        print('查询所有查询编号小于4或没被删除的学生为:')
        for i in results:
            # 打印结果
            print("name = '%s', age = '%s', height = '%s', gender = '%s', cls_id = '%s'" % \
                  (i[1], i[2], i[3], i[4], i[5]))
    except:
        print("Error: unable to fetch data")

# 查询姓黄并且“名”是一个字的学生
def third():
    # 打开数据库连接
    db = pymysql.connect(host="localhost", user="root", password="123456", db="test")

    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    # SQL 查询语句
    sql = "SELECT * FROM students \
                       WHERE name like '黄_'"
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        print('查询姓黄并且“名”是一个字的学生为:')
        for i in results:
            # 打印结果
            print("name = '%s', age = '%s', height = '%s', gender = '%s', cls_id = '%s'" % \
                  (i[1], i[2], i[3], i[4], i[5]))
    except:
        print("Error: unable to fetch data")

# 查询编号是1或3或8的学生
def fouth():
    # 打开数据库连接
    db = pymysql.connect(host="localhost", user="root", password="123456", db="test")

    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    # SQL 查询语句
    sql = "SELECT * FROM students \
                           WHERE id = 1 or id = 3 or id = 8"
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        print('查询编号是1或3或8的学生为:')
        for i in results:
            # 打印结果
            print("name = '%s', age = '%s', height = '%s', gender = '%s', cls_id = '%s'" % \
                  (i[1], i[2], i[3], i[4], i[5]))
    except:
        print("Error: unable to fetch data")

# 查询编号为3至8的学生
def fiveth():
    # 打开数据库连接
    db = pymysql.connect(host="localhost", user="root", password="123456", db="test")

    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    # SQL 查询语句
    sql = "SELECT * FROM students \
                               WHERE id between 3 and 8"
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        print('查询编号为3至8的学生为:')
        for i in results:
            # 打印结果
            print("name = '%s', age = '%s', height = '%s', gender = '%s', cls_id = '%s'" % \
                  (i[1], i[2], i[3], i[4], i[5]))
    except:
        print("Error: unable to fetch data")

# 查询未删除男生信息，按年龄降序
def sixth():
    # 打开数据库连接
    db = pymysql.connect(host="localhost", user="root", password="123456", db="test")

    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    # SQL 查询语句
    sql = "SELECT * FROM students \
    WHERE is_delete = 0 order by age desc"
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        print('查询未删除男生信息，按年龄降序:')
        for i in results:
            # 打印结果
            print("name = '%s', age = '%s', height = '%s', gender = '%s', cls_id = '%s'" % \
                  (i[1], i[2], i[3], i[4], i[5]))
    except:
        print("Error: unable to fetch data")

# 查询女生的总数
def seventh():
    # 打开数据库连接
    db = pymysql.connect(host="localhost", user="root", password="123456", db="test")

    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    # SQL 查询语句
    sql = "SELECT gender, count(*) as num FROM students \
        WHERE gender = '女' group by gender"
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        print('查询女生的总数:')
        print(results)
    except:
        print("Error: unable to fetch data")

# 查询学生的平均年龄
def eighth():
    # 打开数据库连接
    db = pymysql.connect(host="localhost", user="root", password="123456", db="test")

    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    # SQL 查询语句
    sql = "SELECT avg (age) FROM students"
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        print('查询学生的平均年龄:')
        print(results)
    except:
        print("Error: unable to fetch data")

# 分别统计性别为男/女的人年龄平均值
def ninth():
    # 打开数据库连接
    db = pymysql.connect(host="localhost", user="root", password="123456", db="test")

    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    # SQL 查询语句
    sql = "SELECT gender, avg (age) FROM students group by gender"
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        print('分别统计性别为男/女的人年龄平均值:')
        print(results[0],results[1])

    except:
        print("Error: unable to fetch data")

# 按照性别来进行人员分组如下显示（group by + group_concat()）
def tenth():
    # 打开数据库连接
    db = pymysql.connect(host="localhost", user="root", password="123456", db="test")

    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    # SQL 查询语句
    sql = "SELECT gender, GROUP_CONCAT(name) FROM students group by gender"
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        print('按照性别来进行人员分组如下显示:')
        for i in results:
            print('| {} |{}     |'.format(i[0],i[1]))

    except:
        print("Error: unable to fetch data")



if __name__ == '__main__':
    first()
    second()
    third()
    fouth()
    fiveth()
    sixth()
    seventh()
    eighth()
    ninth()
    tenth()