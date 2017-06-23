# 题目：对10个数进行排序。
import random

def sortNum():
    L = []
    for i in range(10):
        L.append(random.randint(1,100))
    L.sort(key=None, reverse=True)
    print(L)


if __name__ == '__main__':
    sortNum()
 