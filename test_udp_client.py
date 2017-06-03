'UDP编程client端'

import socket


def udpClient():
    # 创建socket
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    for data in [b'Michael', b'Tracy', b'Tom', b'Bob', b'Silly']:
        try:
            # 发送数据
            s.sendto(data, ('127.0.0.1', 9992))
            # 接收数据
            print(s.recv(1024).decode('utf-8'))
        except Exception as e:
            print(e)
    s.sendto(b'exit', ('127.0.0.1', 9992))
    s.close()


if __name__ == '__main__':
    udpClient()
