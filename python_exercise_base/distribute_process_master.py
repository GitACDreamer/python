'分布式进程master'

import random
import queue
import logging
import time
import threading
from multiprocessing.managers import BaseManager
from distribute_process_worker import taskWorker

# 发送任务的队列
task_queue = queue.Queue()

# 接收任务的队列
result_queue = queue.Queue()


class QueueManager(BaseManager):
    pass


def return_task_queue():
    global task_queue
    return task_queue


def return_result_queue():
    global result_queue
    return result_queue


def taskMaster():
    # 把两个队列注册到网络上
    QueueManager.register('get_task_queue', callable=return_task_queue)
    QueueManager.register('get_result_queue', callable=return_result_queue)

    # 绑定端口5000，设置验证码
    manager = QueueManager(address=('127.0.0.1', 9543), authkey=b'abc')

    try:
        # 启动Queue
        manager.start()
        time.sleep(1)
    except Exception as e:
        logging.exception(e)

    # 获取通过网络访问的Queue对象
    task = manager.get_task_queue()
    result = manager.get_result_queue()

    # 分配若干任务
    for i in range(10):
        n = random.randint(0, 100)
        print('Put task %d...' % n)
        task.put(n)

    # 从result队列中读取结果
    print('Try get result...')
    for i in range(10):
        r = result.get(timeout=10)
        print('Result: %s' % r)

    # 关闭管理器
    manager.shutdown()
    print('master exit.')


if __name__ == '__main__':
    t1 = threading.Thread(target=taskMaster, name='master')
    t2 = threading.Thread(target=taskWorker, name='worker')
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print('Done……')
