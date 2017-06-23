# 题目：将一个列表的数据复制到另一个列表中。
# 程序分析：使用列表[:]。


def copyList():
    L = []
    [L.append(i) for i in range(10)]
    S = L[:]
    print('L:', L)
    print('S:', S)


if __name__ == '__main__':
    copyList()
