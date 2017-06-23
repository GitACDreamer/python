"""
题目：有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
程序分析：C41*C31*C21=24种,三层循环判断三个数互不相等，也可以用自带的全排列函数
"""
__author__ = 'Leland'

from itertools import permutations


def HandredNum(a, b, c):
    return a * 100 + b * 10 + c


def generateNum():
    L = []
    cnt = 0
    for i in range(1, 5):
        for j in range(1, 5):
            for k in range(1, 5):
                if i != j and i != k and j != k:
                    cnt = cnt + 1
                    L.append(HandredNum(i, j, k))
    print('总共有%d个' % cnt)
    print(L)


def permutation():
    """使用自带全排列函数"""
    print('总共有%d个' % (4 * 3 * 2))
    for n in permutations([1, 2, 3, 4], 3):
        s = ''
        for n0 in n:
            s = s + str(n0)
        print(s)


if __name__ == '__main__':
    generateNum()
    permutation()
