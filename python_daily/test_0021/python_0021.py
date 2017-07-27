# coding=utf-8
# @author: Leland
# @email:  AC_Dreamer@163.com
# @date:   2017-07-25 16:16:18
# @title:  用户密码存储

import uuid
from hashlib import sha256


def encrypt_password(password):
    # uuid is used to generate a random number"""
    salt = uuid.uuid4().hex
    # use sha256 encrypt the password
    return sha256(salt.encode() + password.encode()).hexdigest() + ':' + salt


def check_password(hashed_password, user_password):
    password, salt = hashed_password.split(':')
    # 判断输入的密码和存储的密码生成的哈希值是否相等
    return password == sha256(salt.encode() + user_password.encode()).hexdigest()


if __name__ == '__main__':
    new_password = input('Please input a password: ')
    hashed_password = encrypt_password(new_password)
    print('The string to store in the db is: ' + hashed_password)
    old_password = input('Now please enter the password again to check: ')
    if check_password(hashed_password, old_password):
        print('You enter the right password')
    else:
        print('The password does not match')
