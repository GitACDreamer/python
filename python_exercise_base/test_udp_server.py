'UDP编程server端'

import socket


def udpServer():
    # 创建socket
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 绑定端口
    s.bind(('127.0.0.1', 9992))
    print('Bind UDP on 9992')
    while True:
        # 接收数据
        data, addr = s.recvfrom(1024)
        if not data or data.decode('utf-8') == 'exit':
            break
        print('Received from %s:%s' % addr)
        # 发送数据
        s.sendto(b'Hello ,%s!' % data, addr)
    s.close()


if __name__ == '__main__':
    udpServer()
