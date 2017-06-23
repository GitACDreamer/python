# 斐波那契数列。
# F1 = 1    (n=1)
# F2 = 1    (n=2)
# Fn = F[n-1]+ F[n-2](n>=3)


def FibonacciGen(n):
    if n <= 0:
        raise TypeError('input the number error!')
    i, a, b = 1, 1, 1
    while i <= n:
        if i == 1 or i == 2:
            yield 1
        else:
            a, b = b, a + b
            yield b
        i += 1


def Fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return Fibonacci(n - 1) + Fibonacci(n - 2)


if __name__ == '__main__':
    for i in FibonacciGen(10):
        print(i)

    print('F[%d]=%d' % (10, Fibonacci(10)))
