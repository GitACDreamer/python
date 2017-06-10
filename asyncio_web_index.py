import asyncio

# asyncio的编程模型就是一个消息循环
# 从asyncio模块中直接获取一个EventLoop的引用，然后把需要执行的协程扔到EventLoop中执行，就实现了异步IO。
# 异步操作需要在coroutine中通过yield from完成；
# 多个coroutine可以封装成一组Task然后并发执行。


@asyncio.coroutine
def getIndex(host):
    print('web host: %s' % host)
    connect = asyncio.open_connection(host, 80)
    reader, writer = yield from connect
    header = 'GET / HTTP/1.1\r\nHost: %s\r\n\r\n' % host
    writer.write(header.encode('utf-8'))
    yield from writer.drain()
    while True:
        line = yield from reader.readline()
        if line == b'\r\n':
            break
        print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
    # ignore the body,close the socket
    writer.close()


if __name__ == '__main__':
    # 获取eventLoop
    loop = asyncio.get_event_loop()
    tasks = [getIndex(host) for host in ['www.baidu.com',
                                         'www.sina.com.cn', 'www.sohu.com', 'email.163.com']]
    # 执行coroutine
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()
