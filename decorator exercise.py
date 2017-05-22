import functools

# log的参数时str或者函数
def log(strOrfunc):
    if isinstance(strOrfunc, str):
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kw):
                print('%s(): begian call' % func.__name__)
                func(*args, **kw)
                print('%s(): end call' % func.__name__)
            return wrapper
        return decorator
    else:
        @functools.wraps(strOrfunc)
        def wrapper(*args, **kw):
            print('%s(): begian call' % strOrfunc.__name__)
            strOrfunc(*args, **kw)
            print('%s(): end call' % strOrfunc.__name__)
        return wrapper
@log
def now1():
    print('2017.05.16')


@log('excute')
def now2():
    print('2017.05.16')


def decoratorEx():
    now1()
    now2()
    print(now1.__name__)
    print(now2.__name__)


def main():
    decoratorEx()


if __name__ == '__main__':
    main()
