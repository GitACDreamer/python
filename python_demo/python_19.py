# 题目：一个数如果恰好等于它的因子之和，这个数就称为"完数"。例如6=1＋2＋3.编程找出1000以内的所有完数。


def countNum():
    for n in range(2, 100001, 2):
        sum = 1
        L = [1]
        for i in range(2, int(n / 2 + 1)):
            if n % i == 0:
                sum += i
                L.append(i)
        if sum == n:
            print('完数：', n)
            print(L)


if __name__ == '__main__':
    countNum()
