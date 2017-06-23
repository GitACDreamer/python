'分布式进程worker'

import sys
import time
import queue
from multiprocessing.managers import BaseManager


class QueueManager(BaseManager):
    pass


def taskWorker():
    QueueManager.register('get_task_queue')
    QueueManager.register('get_result_queue')

    manager = QueueManager(address=('127.0.0.1', 9543), authkey=b'abc')

    # 连接服务器
    manager.connect()

    task = manager.get_task_queue()
    result = manager.get_result_queue()

    # get connect from task queue and return new result to result queue
    for i in range(10):
        try:
            n = task.get(timeout=1)
            print('run task %d*%d...' % (n, n))
            r = '%d*%d=%d' % (n, n, n * n)
            time.sleep(1)
            result.put(r)
        except queue.Empty:
            print('task queue is empty...')
    print('worker exit...')
