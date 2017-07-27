def consumer():
    r = ''
    while True:
        n = yield r  # jump to producer
        if not n:
            return
        print('[consumer] consuming %s……' % n)
        r = '200 OK'


def producer(c):
    c.send(None)
    n = 0
    while n < 5:
        n += 1
        print('[Producer] produce %s……' % n)
        r = c.send(n)  # jump to consumer
        print('[Producer] Consumer return: %s' % r)
    c.close()


if __name__ == '__main__':
    c = consumer()
    producer(c)
