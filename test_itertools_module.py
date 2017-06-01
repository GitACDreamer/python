'itertools 的使用'
# itertools模块提供的全部是处理迭代功能的函数，它们的返回值不是list，而是Iterator，只有用for循环迭代的时候# 才真正计算

import itertools

def testItertools():
    # 1~n的自然数
    naturals = itertools.count(1)
    # for n in naturals:
    #     print(n)
    print(list(itertools.takewhile(lambda x: x < 20, naturals)))

    # ABCDE循环显示
    cs = itertools.cycle('ABCDE')
    # for c in cs:
    #     print(c)

    # 重复显示(10次，默认无数次)
    ns = itertools.repeat('B', 5)
    for n in ns:
        print(n)

    # 将一组迭代对象串联起来
    for c in itertools.chain('ABCDE', 'XYZ', '123'):
        print(c)

    # 将迭代器中相邻的重复元素挑出来放一起
    for key, group in itertools.groupby('AAAABBBBCCCCCCDDDEEAAACCC'):
        print(key, list(group))

    # 不区分大小写
    for key, group in itertools.groupby('AaaBBbbccCCaA', lambda c: c.lower()):
        print(key, list(group))


if __name__ == '__main__':
    testItertools()
