'base64的使用'
# Base64是一种任意二进制到文本字符串的编码方法，常用于在URL、Cookie、网页中传输少量二进制数据。

import base64
import re


def safe_base64_decode(s):
    # 编码时是3个字节一组，所以字节缺失可能有一个或两个，也就是等号最多有一个或两个
    if not len(s) % 4 == 0:
        s = s + b'=' * (4 - len(s) % 4)
    return base64.b64decode(s)


def testBase64():
    # encode
    print(base64.b64encode(b'binary\x00string'))
    # decode
    print(base64.b64decode(b'YmluYXJ5AHN0cmluZw=='))
    # 由于标准的Base64编码后可能出现字符+和/，在URL中就不能直接作为参数，所以又有一种"url safe"的base64编# 码，其实就是把字符+和/分别变成-和_
    # encode
    print(base64.b64encode(b'i\xb7\x1d\xfb\xef\xff'))
    # safe encode
    print(base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff'))
    # safe decode
    print(base64.urlsafe_b64decode('abcd--__'))
    print(base64.b64encode(b'abcd'))
    print(safe_base64_decode(b'YWJjZA'))


if __name__ == '__main__':
    testBase64()
