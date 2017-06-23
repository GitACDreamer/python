'多线程、多进程,异步IO测试'

import time
import requests
import threading
import multiprocessing
import asyncio
import aiohttp


def single_process():
    # 单进程

    start = time.time()
    [requests.get('http://www.baidu.com') for x in range(100)]
    print('single_process host: {}s'.format(time.time() - start))


def run(url):
    [requests.get(url=url) for x in range(100)]


def multi_thread():
    # 多线程

    start = time.time()
    t = threading.Thread(target=run, args=('http://www.baidu.com',))
    t.start()
    t.join()
    print('multi_thread host: {}s'.format(time.time() - start))


def multi_process():
    # 多进程

    start = time.time()
    pool = multiprocessing.Pool(10)
    [pool.apply_async(run, args=('http://www.baidu.com',))]
    pool.close()
    pool.join()
    print('multi_process host: {}s'.format(time.time() - start))


def async_io():
    # 异步IO(效率最高)

    start = time.time()

    async def run(url):
        async with aiohttp.ClientSession() as session:
            async with session.get(url=url) as resp:
                pass
    loop = asyncio.get_event_loop()
    tasks = [asyncio.ensure_future(run('http://www.baidu.com'))
             for x in range(100)]
    loop.run_until_complete(asyncio.wait(tasks))
    print('async_io host: {}s'.format(time.time() - start))


def main():
    single_process()
    multi_thread()
    multi_process()
    async_io()

    # single_process host: 4.630264759063721s
    # multi_thread host: 4.436253786087036s
    # multi_process host: 9.557546854019165s
    # async_io host: 0.7820446491241455s

if __name__ == '__main__':
    main()
