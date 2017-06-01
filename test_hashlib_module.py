'摘要算法'
# 摘要算法在很多地方都有广泛的应用。要注意摘要算法不是加密算法，不能用于加密（因为无法通过摘要反推明文），只#
# 能用于防篡改，但是它的单向计算特性决定了可以在不存储明文口令的情况下验证用户口令。

import hashlib

db = {}


def get_md5(username, password):
    salt = 'administrator'
    return hashlib.md5((password + username + salt).encode('utf-8')).hexdigest()


def register(username, password):
    db[username] = get_md5(username, password)

def login(username, password):
    if db[username] == get_md5(username, password):
        print('Success')
    else:
        print('Default')


def testHashlib():
    md5 = hashlib.md5()
    md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
    print(md5.hexdigest())

    # 如果数据量很大，可以分块多次调用update()，最后计算的结果是一样的
    md5 = hashlib.md5()
    md5.update('how to use md5 in '.encode('utf-8'))
    md5.update('python hashlib?'.encode('utf-8'))
    print(md5.hexdigest())

    d = {'liming': '12345', 'lihua': 'abcdef',
         'huawang': 'ccedf', 'liliang': 'asdfghjkl'}
    for k, v in d.items():
        register(k, v)

    d['liliang'] = 'abcdefg'
    for k, v in d.items():
        login(k, v)


if __name__ == '__main__':
    testHashlib()
