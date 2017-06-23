# 输出 9*9 乘法口诀表。


def multipleTable():
    for i in range(1, 10):
        for j in range(1, i + 1):
            if i != j:
                print('%d*%d=%d' % (i, j, i * j), sep=' ', end=' ')
            else:
                print('%d*%d=%d' % (i, j, i * j))


if __name__ == '__main__':
    multipleTable()
