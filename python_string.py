def main():
    # 获取字符的整数
    print(ord('A'))
    print(ord('你'))
    # 获取编码对应的字符
    print(chr(77))
    print(chr(25991))
    # 已知字符的编码
    print('\u4e2d\u6587')
    x = b'ABC'
    print(x)
    # 设置编码格式
    print('ABC'.encode('ascii'))
    print( '中文'.encode('utf-8'))
    # 字符串中包含中文时，不能设置为ascii格式，中文编码超过ascii编码的范围了
    # UnicodeEncodeError: 'ascii' codec can't encode characters in position 0-1:
    # ordinal not in range(128)
    # print('中文'.encode('ascii'))

    # 从网络或者磁盘读取字节流
    print(b'ABC'.decode('ascii'))
    print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))

    # 计算字符串的长度
    print(len('ABC'))
    # 1个中文字符经过UTF-8编码后通常会占用3个字节，而1个英文字符只占用1个字节
    print(len('中文'.encode('utf-8')))

if __name__ == '__main__':
    main()