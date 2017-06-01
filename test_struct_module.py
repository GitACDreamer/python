'struct 的使用'

import struct


def testStruct():
    n = 10240099
    b1 = (n & 0xff000000) >> 24
    b2 = (n & 0xff0000) >> 16
    b3 = (n & 0xff00) >> 8
    b4 = n & 0xff
    bs = bytes([b1, b2, b3, b4])
    print(bs)

    # >表示字节顺序是big-endian，也就是网络序，I表示4字节无符号整数。
    print(struct.pack('>I', 10240099))

    # >IH的说明，后面的bytes依次变为I：4字节无符号整数和H：2字节无符号整数
    print(struct.unpack('>IH', b'\xf0\xf0\xf0\xf0\x80\x80'))


if __name__ == '__main__':
    testStruct()
