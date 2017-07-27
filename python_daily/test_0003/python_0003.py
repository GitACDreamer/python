# 将 python_0001 题生成的 200 个激活码（或者优惠券）保存到 MySQL 关系型数据库中。

import pymysql
import logging
import uuid


def save_data_to_db():
    try:
        # 连接数据库
        conn = pymysql.connect(host='localhost', port=3306, user='root',
                               passwd='123456', db='student', charset='utf8')
        # 设置自动提交
        conn.autocommit(True)

        # 获取游标
        cursor = conn.cursor()

        # 创建数据表
        create_table(conn, cursor)

        # 插入数据
       # insert_data(conn, cursor)

        # 查询数据
        query_data(conn, cursor)
    finally:
        # 关闭数据库
        conn.close()


def create_table(conn, cursor):
    try:
        sql = 'create table if not exists ativation_code (id int primary key AUTO_INCREMENT, code varchar(255))'
        cursor.execute(sql)
        conn.commit()
    except Exception as e:
        logging.error(e)
        cursor.close()
        conn.rollback()


def create_code(num=200):
    codes = []
    while True:
        code = str(uuid.uuid1()).replace('-', '')
        if not code in codes:
            codes.append(code)
        if len(codes) is num:
            break
    return codes


def insert_data(conn, cursor):
    try:
        # 获取生成的数据
        codes = create_code(200)
        for code in codes:
            cursor.execute(
                'insert into ativation_code(code) value(%s)', (code))
        conn.commit()
    except Exception as e:
        logging.error(e)
        cursor.close()
        conn.rollback()


def query_data(conn, cursor):
    try:
        # 查询数据
        cursor.execute('select code from ativation_code limit %s', 20)
        data = cursor.fetchall()
        for d in data:
            print(d)
    except Exception as e:
        logging.error(e)
        cursor.close()
        conn.rollback()


if __name__ == '__main__':
    save_data_to_db()
