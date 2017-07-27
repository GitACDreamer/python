'异常处理'
# 所有的错误类型都继承自BaseException，所以在使用except时需要注意的是，它不但捕获该类型的错误，还把其子类也“一网打尽”

import logging

def exceptTest():
    try:
        print('try...')
        r = 10 / 'a'
        print('result:', r)
    except ZeroDivisionError as e:
        print('except:', e)
    except ValueError as e:
        print('ValueError:', e)
    except TypeError as e:
        print('TypeError:', e)
        logging.exception(e)
    finally:
        print('finally……')
    print('END')


def foo(s):
    return 10 / int(s)


def bar(s):
    return foo(s) * 2


def exceptTest2():
    try:
        bar('0')
    except Exception as e:
        print('Error:', e)
    finally:
        print('finally……')

# 抛出异常
class FooError(ValueError):
    pass


def func(s):
    n = int(s)
    if n == 0:
        raise FooError('invalid value: %s' % s)
    return 10 / n


def fun2():
    try:
        func('0')
    except ValueError as e:
        print('ValueError!')
        raise

def assertTest():
    n = 0
    assert n != 0 , 'n is zero'
    return 10/n

def main():
    exceptTest()
    exceptTest2()
    try:
        func('0')
        fun2()
    except Exception as e:
        print('Exception:' ,e)
    assertTest()

if __name__ == '__main__':
    main()
