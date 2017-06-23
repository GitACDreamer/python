# 题目：有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和。


def Fibonacci(n):
    i, a, b = 1, 1, 1
    if n == 1 or n == 2:
        yield 1
    while i <= n:
        if i == 1 or i == 2:
            yield 1
        else:
            a, b = b, a + b
            yield b
        i += 1


def calcSum(n):
    L = []
    for i in Fibonacci(n + 2):
        L.append(i)
    print(L)
    sum = 0
    for i in range(1, n + 1):
        sum += (L[i + 1] / L[i])
    print(sum)


def calcS():
    a, b = 1, 2
    sum = 0
    for i in range(20):
        sum += b / a
        a, b = b, a + b
    print(sum)


if __name__ == '__main__':
    # calcSum(20)
    calcS()
