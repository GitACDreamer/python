'TCP编程服务器端'
# 80端口是Web服务的标准端口。其他服务都有对应的标准端口号，例如SMTP服务是25端口，FTP服务是21端口，等等。端口# 号小于1024的是Internet标准服务的端口，端口号大于1024的，可以任意使用

import socket
import threading
import time


def soketServer():
    """ 服务器端
    """
    # 创建连接
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 监听端口
    s.bind(('127.0.0.1', 9544))
    # 开始监听
    print('Waiting for connection……')
    # 监听最多5个客户端
    s.listen(5)

    while True:
        # 接收一个新的连接
        sock, addr = s.accept()
        # 创建新的线程来处理TCP连接
        t = threading.Thread(target=tcpLink, args=(sock, addr))
        t.start()


def tcpLink(sock, addr):
    print('Accept name connection from %s:%s' % addr)
    sock.send(b'Welcome')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('Hello,%s!' % data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print('Connection from %s:%s closed' % addr)


if __name__ == '__main__':
    soketServer()
