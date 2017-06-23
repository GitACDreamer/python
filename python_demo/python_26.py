# 题目：利用递归方法求n!。


def classN(n):
    if n == 1 or n == 0:
        return 1
    else:
        return classN(n - 1) * n


if __name__ == '__main__':
    print(classN(5))
