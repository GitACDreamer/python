'TCP编程客户端'

import socket
import threading
import time


def socketClient():
    """客户端
    """
    # 创建一个socket连接
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        # 建立连接
        s.connect(('127.0.0.1', 9544))
        # 接收到服务器的欢迎消息
        print(s.recv(1024).decode('utf-8'))

        # 发送和接收消息
        for data in [b'Micheal', b'Bob', b'Tom', b'Silly']:
            # 发送消息
            s.send(data)
            # 接收消息
            print(s.recv(1024).decode('utf-8'))
        s.send(b'exit')
    except Exception as e:
        print(e)
    s.close()


if __name__ == '__main__':
    socketClient()
