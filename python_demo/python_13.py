# 题目：打印出所有的"水仙花数"，所谓"水仙花数"是指一个三位数，其各位数字立方和等于该数本身。例如：153是一个 #
# "水仙花数"，因为153=1的三次方＋5的三次方＋3的三次方。

import math


def isNarcissisticNumber(n):
    i = int(n / 100)
    j = int(n / 10 % 10)
    k = n % 10
    if math.pow(i, 3) + math.pow(j, 3) + math.pow(k, 3) == n:
        return True
    else:
        return False


if __name__ == '__main__':
    for i in range(100, 999):
        if isNarcissisticNumber(i):
            print(i)
