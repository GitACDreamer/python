import math


def test():
    # abs
    print('abs(x)=', abs(-5))
    # max
    print('max(1,3,2,-4,0)=', max(1, 3, 2, -4, 0))
    # main
    print('min(1,3,2,-4,0)=', min(1, 3, 2, -4, 0))
    # max
    print('max(\'a\',\'b\',\'c\',\'d\')=', max('a', 'b', 'c', 'd'))

    # 进制转换
    print('hex(110)=', hex(110))
    print('hex(12)=', hex(12))

    # 类型转换
    print('int(1.2)=', int(1.2))
    print('str(10)=', str(10))

    # 函数取别名
    # 函数名其实就是指向一个函数对象的引用，完全可以把函数名赋给一个变量，相当于给这个函数起了一个“别名”
    ABS = abs
    print('ABS(-4)=', ABS(-4))

    # 调用函数
    print('my_abs(-55)=', my_abs(-55))
    # print('my_abs(\'A\')=', my_abs('A'))

    # 空函数
    nop()

    # 函数返回多个值
    print('move(100 , 200 , 40 , 60)=', move(100, 200, 40, math.pi / 3))

    # 求二元一次方程的解
    print('(x^2-5x+6=0)的解：', quadratic(1, -5, 6))
    print('(x^2+x+1)=', quadratic(1, 1, 1))



def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operant type')
    if x >= 0:
        return x
    else:
        return -x


def nop():
    pass


def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y + step * math.sin(angle)
    return nx, ny


# 求二元一次方程的两个根
def quadratic(a, b, c):
    t = b * b - 4 * a * c
    if t < 0 or a == 0:
        return '此方程无解'
    x1 = (-b + math.sqrt(b * b - 4 * a * c)) / (2 * a)
    x2 = (-b - math.sqrt(b * b - 4 * a * c)) / (2 * a)
    return x1, x2


def main():
    test()


if __name__ == '__main__':
    main()
