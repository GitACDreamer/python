# 高阶函数
# 编写高阶函数，就是让函数的参数能够接收别的函数。
from math import sqrt
def absAdd(x,y,f):
    return f(x) + f(y)

# 绝对值的平方根
def absSqrt(x , *fs):
    for f in fs:
        x = f(x)
    return x

def main():
    print(absAdd(10 , -11 ,abs))

    print(absSqrt(-4 , abs , sqrt))

if __name__ == '__main__':
    main()