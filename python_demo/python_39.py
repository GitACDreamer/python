# 题目：有一个已经排好序的数组。现输入一个数，要求按原来的规律将它插入数组中。
# 分析：二分法查找
import random


def findIndex(L, num):
    start, end, mid = 0, len(L) - 1, int(len(L) / 2)
    while start < end:
        if L[mid] > num:
            end = mid - 1
        else:
            start = mid + 1
        mid = (int)((start + end) / 2)
    return mid if L[mid] > num else mid + 1


def insertNewNumberToSortedList():
    L = []
    for i in range(10):
        L.append(random.randint(1, 100))
    # 已排序序列
    L.sort()
    # 需要插入的随机数
    a = random.randint(1, 100)
    print('原列表：\n', L)
    print('要插入的数：', a)
    index = findIndex(L, a)
    L.insert(index, a)
    print(L)


if __name__ == '__main__':
    insertNewNumberToSortedList()
