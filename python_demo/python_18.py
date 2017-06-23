# 题目：求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数
# 相加由键盘控制。

import math

def calcSum(n, a):
    sum = 0
    t = 0
    for j in range(n):
        t += a * math.pow(10, j)
        sum += t
    return sum


if __name__ == '__main__':
    n = int(input('输入n：'))
    a = int(input('输入a：'))
    print('sum=%d' % calcSum(n, a))
