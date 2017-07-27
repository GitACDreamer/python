# -*- coding: utf-8 -*-
# 第 0003 题：将 0001 题生成的 200 个激活码（或者优惠券）保存到 Redis 非关系型数据库中。

import redis
import uuid

redis_server = redis.StrictRedis(host='localhost', port=6379, db=0)


def create_code(num=200):
    """生成200个激活码"""
    codes = []
    while True:
        code = str(uuid.uuid1()).replace('-', '')
        if not code in codes:
            codes.append(code)
        if(len(codes) is num):
            break
    return codes


def clean_up(prefix='random_codes'):
    """删除所有的数据"""
    keys = redis_server.keys('%s_*' % prefix)
    for key in keys:
        redis_server.delete(key)


def insert_code(code, prefix='random_codes'):
    """插入一条记录"""
    redis_server.set('%s_%s' % (prefix, code), code)


def select_code(prefix='random_codes'):
    """查询所有的记录"""
    keys = redis_server.keys('%s_*' % prefix)
    codes = []
    for key in keys:
        codes.append(redis_server.get(key))
    return codes


def process():
    # 清除所有数据
    clean_up()
    # 生成200条数据
    codes = create_code()
    # 插入200条记录
    for code in codes:
        insert_code(code)
    return codes


if __name__ == '__main__':
    try:
        process()
    except Exception as e:
        print(e)
