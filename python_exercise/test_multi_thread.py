'多线程'

# 多线程编程，模型复杂，容易发生冲突，必须用锁加以隔离，同时，又要小心死锁的发生。
# Python解释器由于设计时有GIL全局锁，导致了多线程无法利用多核。多线程的并发在Python中就是一个美丽的梦。

import threading
import time

# 线程执行代码
def loop():
    print('thread %s is running……' % threading.current_thread().name)
    n = 0
    while n < 5:
        n = n + 1
        print('thread %s >>>%s' % (threading.current_thread().name, n))
        time.sleep(1)
    print('thread %s is ended' % threading.current_thread().name)


def multiThread():
    print('thread %s is running……' % threading.current_thread().name)
    t = threading.Thread(target=loop, name='LoopThread')
    t.start()
    t.join()
    print('thread %s is ended.' % threading.current_thread().name)


# 多线程共享数据(可能会出错的情况),所以需要关键代码上锁
balance = 0
lock = threading.Lock()


def change_it(n):
    global balance
    # 先增后减
    balance += n
    balance -= n


def run_thread(n):
    for i in range(100000):
        # 先申请获取锁
        lock.acquire()
        try:
            # 方向的修改值
            change_it(n)
        finally:
            # 执行完释放锁
            lock.release()


def shareData():
    t1 = threading.Thread(target=run_thread, args=(5,))
    t2 = threading.Thread(target=run_thread, args=(11,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print('balance=', balance)


def main():
    shareData()
    multiThread()


if __name__ == '__main__':
    main()
