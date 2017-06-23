# 题目：判断101-200之间有多少个素数，并输出所有素数。
# 程序分析：判断素数的方法：用一个数分别去除2到sqrt(这个数)，如果能被整除，则表明此数不是素数，反之是素数。

import math


def isPrime(n):
    if n == 2:
        return True
    else:
        for i in range(2, int(math.sqrt(n) + 1)):
            if n % i == 0:
                return False
        return True


if __name__ == '__main__':
    for i in range(101, 200):
        if isPrime(i):
            print(i)
