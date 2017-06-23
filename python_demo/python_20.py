# 题目：一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第
# 10次反弹多高？


def calcPath():
    sum = 0
    a = 100
    for i in range(1, 11):
        if i == 1:
            sum += a
        else:
            sum += a * 2
        a /= 2
    print('总共经过{}米，第10次反弹{}'.format(sum, a))


if __name__ == '__main__':
    calcPath()
