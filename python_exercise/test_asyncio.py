import threading
import asyncio


@asyncio.coroutine
def hello():
    print('Hello,World! (%s)' % threading.currentThread())
    yield from asyncio.sleep(2)  # sleep 1 s
    print('Hello Again! (%s)' % threading.currentThread())


if __name__ == '__main__':
    # 由打印的当前线程名称可以看出，两个coroutine是由同一个线程并发执行的。
    loop = asyncio.get_event_loop()
    tasks = [hello(), hello()]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()
