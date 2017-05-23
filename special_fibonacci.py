'定制Fibonacci类'

class Fibonacci(object):
    __MAX_VALUE = 10000
    def __init__(self):
        self.__a , self.__b = 0,1 # 初始化两个计数器
    def __iter__(self):
        return self  # 实例本身是迭代器，返回本身
    def __next__(self):
        self.__a , self.__b = self.__b , self.__a + self.__b  # 计算下一个值
        if self.__a > self.__MAX_VALUE:  #退出循环的条件
            raise StopIteration()
        return self.__a  # 返回下一个值
    def __getitem__(self , n):
        if isinstance(n , int):  # n是索引
            a , b = 1,1
            for x in range(n):
                a, b = b , a+b
            return a
        elif isinstance(n , slice):
            start = n.start
            end = n.stop
            if start is None:
                start = 0
            a , b = 1,1
            L = []
            for x in range(end):
                if x >= start:
                    L.append(a)
                a , b = b , a+b
            return L
        else:
            raise TypeError('input the error type')
            

def main():
   f = Fibonacci()
   print(f[0])
   print(f[2])
   print(f[8])
   print(f[:10])
   # print(f['a'])
   for n in f:
       print(n)

if __name__ == '__main__':
    main()