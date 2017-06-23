# 题目：输入三个整数x,y,z，请把这三个数由小到大输出。


def sortNum():
    L = []
    L.append(int(input('x:')))
    L.append(int(input('y:')))
    L.append(int(input('z:')))
    L.sort()
    for i in L:
        print(i)


if __name__ == '__main__':
    sortNum()
