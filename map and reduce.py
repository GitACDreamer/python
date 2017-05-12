# map()函数接收两个参数，一个是函数，一个是Iterable
# reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算，
# 其效果就是：reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)

from functools import reduce


def mapAndReduce():
    L1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(L1)

    # 对每个元素进行平方
    print(list(map(f, L1)))

    # 将整数转换成字符串
    print(list(map(str, L1)))

    # reduce 的使用
    print(reduce(fn, L1))

    # str2Int
    print(str2Int('12345'))

    # lambda 语法格式
    print(strToInt('1456789'))

    # 变成首字母大写，其余的小写
    print(textCapWord(['aDKLF','abd','AADJLKD' , 'E2kd']))

    #list所有元素求积
    print(prod([1,2,3,4,5]))

    # 字符串转float
    print(str2float2('1000.005'))

def f(x):
    return x * x


def fn(x, y):
    return x * 10 + y

def char2Num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s];

def str2Int(s):
    return reduce(fn, map(char2Num, s))

def normalize(s):
   return s.capitalize()

def textCapWord(s):
    return list(map(normalize , s))

# 所有list元素求积
def prod(L):
    return reduce(lambda x, y: x*y , L)

# lambda 语法
def strToInt(s):
    def char2Num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s];
    return reduce(lambda x, y: 10 * x + y, map(char2Num, s))

def str2float2(s):
    # reduce(整数部分+ 小数部分【小数部分= 小数转换的整数*10^(小数点的位数)】)
    # 例如： 123,345 reduce(123 + 345*(10^-3) , map(两部分的字符串分别转整数))
    return reduce(lambda x,y: x+ y*pow(10, -1*len(s.split('.')[1])) ,  map(int , s.split('.')))

def main():
    mapAndReduce()


if __name__ == '__main__':
    main()
