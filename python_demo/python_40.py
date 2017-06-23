# 题目：将一个数组逆序输出。

import random


def showReserse():
    L = []
    for i in range(10):
        L.append(random.randint(1, 100))
    print(L)
    print(L[::-1])


if __name__ == '__main__':
    showReserse()
