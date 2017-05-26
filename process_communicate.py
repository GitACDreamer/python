'进程间的通信'

from multiprocessing import Process, Queue
import os
import time
import random

# 写数据进程


def write_data(q):
    print('Process to write: %s' % os.getpid())
    for value in ['A', 'B', 'C','D']:
        print('Put %s to queue...' % value)
        q.put(value)
        time.sleep(random.random())

# 读数据进程


def read_data(q):
    print('Process to read: %s' % os.getpid())
    while True:
        value = q.get(True)
        print('Get %s from queue.' % value)


def test_communicate():
    # 父进程创建Queue,并传给各自子进程
    q = Queue()
    pw = Process(target=write_data, args=(q,))
    pr = Process(target=read_data, args=(q,))
    # 启动子进程写入
    pw.start()
    # 启动子进程读取
    pr.start()
    # 等待pw写入完毕
    pw.join()
    # pr进程里是死循环，无法等待其结束，只能强行终止:
    pr.terminate()

def main():
    test_communicate()


if __name__ == '__main__':
    main()
