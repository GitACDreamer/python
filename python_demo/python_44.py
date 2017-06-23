# 两个二维矩阵相加，并返回一个新矩阵：

import numpy as np
import random


def generateMatrix():
    A = []

    for i in range(5):
        X = []
        for j in range(5):
            X.append(random.randint(1, 100))
        A.append(X)
    return A


def addMatrix():
    A = generateMatrix()
    B = generateMatrix()

    print('A：', A)
    print('B：', B)
    C = np.array(A) + np.array(B)
    print('C：', C)


if __name__ == '__main__':
    addMatrix()
