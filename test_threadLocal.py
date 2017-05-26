'TheadLocal 的使用'
# 一个ThreadLocal变量虽然是全局变量，但每个线程都只能读写自己线程的独立副本，互不干扰。ThreadLocal解决了参# 数在一个线程中各个函数之间互相传递的问题。(类似于每个对象自己对于的this指针)

import threading

local_name = threading.local()

def process_student():
    # 获取当前线程相关的name
    std = local_name.name
    print('Hello , %s (in %s)' % (std, threading.current_thread().name))


def process_thread(name):
    # 绑定ThreadLocal的name
    local_name.name = name
    process_student()


def main():
    t1 = threading.Thread(target=process_thread,
                          args=('Alice',), name='Thead-A')
    t2 = threading.Thread(target=process_thread,
                          args=('Bob',), name='Thread-B')
    t1.start()
    t2.start()
    t1.join()
    t2.join()


if __name__ == '__main__':
    main()