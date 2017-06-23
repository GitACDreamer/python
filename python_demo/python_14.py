# 题目：将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。

import math
import time


def isPrime(n):
    if n == 2 or n == 3:
        return True
    else:
        for i in range(2, int(math.sqrt(n) + 1)):
            if n % i == 0:
                return False
        return True


def listPrime():
    # 打表的方式效率不高！！！
    while True:
        #a0 = n = int(input('请输入大于等于2的数字：'))
        a0 = n = 9279874928789472
        t0 = time.time()
        if isPrime(n):
            print('%d=%d' % (n, n))
        else:
            L = []
            S = []
            for i in range(2, int(math.sqrt(n) + 1)):
                if isPrime(i):
                    L.append(i)
            while not isPrime(n):
                for v in L:
                    if isPrime(n):
                        break
                    if(n % v == 0):
                        n = n / v
                        S.append(v)
                    elif n <= v:
                        break
            S.append(n)
            print('%d=' % a0, sep=' ', end='')
            for i in range(len(S)):
                if i < len(S) - 1:
                    print('%d*' % S[i], sep='', end='')
                else:
                    print('%d' % S[i])
        t1 = time.time()
        print('host:', t1 - t0)


def listPrimeData():
    while True:
        t0 = time.time()
        a0 = n = int(input('请输入大于等于2的数字：'))
        #a0 = n = 9279874928789472
        if isPrime(n):
            print('%d=%d' % (n, n))
        else:
            L = []
            while n > 1:
                for i in range(2, int(math.sqrt(n) + 1)):
                    if n % i == 0:
                        n = n / i
                        L.append(str(i))
                        break
                if isPrime(n):
                    break
            L.append(str(int(n)))
            print('%d=' % (a0) + '*'.join(L))
        t1 = time.time()
        print('host:', t1 - t0)


if __name__ == '__main__':
    listPrimeData()
