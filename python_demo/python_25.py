# 题目：求1+2!+3!+...+20!的和。


def calcClass():
    sum = 0
    a = 1
    for i in range(1, 21):
        a *= i
        sum += a
    print(sum)


if __name__ == '__main__':
    calcClass()
