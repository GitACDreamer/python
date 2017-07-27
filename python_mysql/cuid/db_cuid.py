# coding=utf-8
# @author: Leland
# @email:  AC_Dreamer@163.com
# @date:   2017-07-27 10:38:52
# @title:  connect mysql database

import pymysql
from read_db_config import read_db_config


def connect():
    """ Connect to MySQL database """
    db_config = read_db_config()
    print(db_config)
    try:
        print('Connecting to MySQL database...')
        # connect mysql database
        conn = pymysql.connect(
            host=db_config['host'], user=db_config['user'], passwd=db_config['password'], db=db_config['database'], port=int(db_config['port']), charset=db_config['charset'], autocommit=bool(db_config['autocommit']))
        # create cursor
        cursor = conn.cursor()

        # query data
        query_data(cursor)

        # insert data
        insert_data(conn, cursor)

        # update data
        update_data(conn, cursor)

        # delete data 
        delete_data(conn , cursor)
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()
        print('Connection closed.')


def query_data(cursor):
    try:
        sql = 'select * from student'
        cursor.execute(sql)
        print('Query data from mysql……')
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except Exception as e:
        raise Exception('query data error: ', e)


def insert_data(conn, cursor):
    try:
        students = [[1008, 'Apple', 96, 25, 'M'],
                    [1009, 'Cuuz', 47, 25, 'F'],
                    [1010, 'Banana', 79, 23, 'M'],
                    [1011, 'Asshole', 58, 30, 'F'],
                    [1012, 'Beeper', 39, 17, 'F']]
        for student in students:
            sql = 'insert into student(number , name , score , age , gender) values(%s,%s,%s,%s,%s)'
            cursor.execute(
                sql, (student[0], student[1], student[2], student[3], student[4]))
            conn.commit()
        print('insert data to database……')
    except Exception as e:
        conn.rollback()
        raise Exception('insert data error: ', e)


def update_data(conn, cursor):
    try:
        sql = 'update student set name = %s where id = %s'
        cursor.execute(sql, ('coldplay', 9))
        conn.commit()
        print('update data to database……')
    except Exception as e:
        conn.rollback()
        raise Exception('insert data error: ', e)

def delete_data(conn, cursor):
    try:
        sql = 'delete from student where id = %s'
        cursor.execute(sql, 17)
        conn.commit()
        print('delete data to database……')
    except Exception as e:
        conn.rollback()
        raise Exception('insert data error: ', e)

def stored_procedure():
    DELIMITER $$
    DELIMITER
if __name__ == '__main__':
    connect()
