# 题目：求100之内的素数。

import math


def isPrime(n):
    if n == 2:
        return True
    for i in range(2, (int)(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True


if __name__ == '__main__':
    for i in range(2, 101):
        if isPrime(i):
            print(i)
