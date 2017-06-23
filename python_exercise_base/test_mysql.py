'mysql的使用'
# MySQL的SQL占位符是%s。
# 执行INSERT,DELETE,UPDATE等操作后要调用commit()提交事务；

import pymysql


def testMysql():

    try:
        # 打开数据库连接
        conn = pymysql.connect("localhost", "root", "123456", "student")

        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = conn.cursor()

        # 使用 execute()  方法执行 SQL 查询
        cursor.execute("SELECT VERSION()")

        # 使用 fetchone() 方法获取单条数据.
        data = cursor.fetchone()

        # 显示版本号
        print("Database version : %s " % data)
    except Exception as e:
        print(e)
    finally:
        # 关闭数据库连接
        conn.close()


def testQueryStudent():
    try:
        conn = pymysql.connect("localhost", "root", "123456", "student")

        cursor = conn.cursor()

        # 查询数据
        cursor.execute(
            'select * from student where score between %d and %d order by score asc' % (60, 100))
        data = cursor.fetchall()
        print(data)
        try:
            # 插入数据(参数都要用%s,不能用%d,%f等等)
            cursor.execute('insert into student values(%s,%s,%s,%s,%s,%s)',
                           (7, "1007", "Google", 80, 18, 'M'))
            conn.commit()
        except Exception as error:
            print(error)
            conn.rollback()
        # 更新数据
        try:
            cursor.execute(
                'update student set number = %s , name = %s where id = %s', ('1004', 'Pame', 4))
            conn.commit()
        except Exception as error:
            print(error)
            conn.rollback()
        # 查询数据
        cursor.execute(
            'select * from student where score between %d and %d order by score asc' % (50, 100))
        data = cursor.fetchall()
        print(data)
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.commit()
        conn.close()


if __name__ == '__main__':
    testMysql()
    testQueryStudent()
