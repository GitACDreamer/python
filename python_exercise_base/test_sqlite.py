'使用数据库'
# sqlite的占位符是?
import sqlite3


def testDB():

    try:
        # 创建数据库
        conn = sqlite3.connect('student.db')
        # 创建一个cursor
        cursor = conn.cursor()
        # 判断表是否存在，如果存在则删除
        # cursor.execute('drop table if exists student')
        # 创建一个表student(创建表，如果不存在的话)
        cursor.execute(
            'create table if not exists student (id int primary key , num varchar(20) , name varchar(100) , score int)')
        nums = ['1001', '1002', '1003', '1004', '1005']
        names = ['Tom', 'Bob', 'Machael', 'July', 'Jon']
        scores = [100, 83, 94, 79, 85]
        for i in range(5):
            cursor.execute('insert into student (id , num , name , score) values(?,?,?,?)',
                           (i, nums[i], names[i], scores[i]))
        # 查询所有数据
        cursor.execute('select * from student')
        values = cursor.fetchall()
        print(values)
        # between ? and ? order by score asc
        # 查询分数大于90的,按分数排序
        cursor.execute(
            'select * from student where score >= ? order by score asc', (90,))
        values = cursor.fetchall()
        print(values)
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.commit()
        conn.close()


if __name__ == '__main__':
    testDB()
