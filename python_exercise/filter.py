def filterTest():
    L1 = list(range(10))
    #求序列中的奇数
    print(list(filter(is_odd, L1)))

    # 求1000以内的素数
    print(list(prime(1000)))

    print(list(huiwen(1000)))

def is_odd(n):
    return n % 2 == 1

# 构造一个大于3的奇数iter
def iter_odd():
    n = 1
    while True:
        n = n + 2
        yield n

# 构造一个不能被整除的筛选器
def not_divisiable(n):
    return lambda x: x % n > 0

# 求素数2~n 的素数
def prime(x):
    yield 2
    it = iter_odd()      # 返回序列的第一个数
    while True:
        n = next(it)
        if n > x:
          break
        yield n          # 返回序列的第n个数
        it = filter(not_divisiable(n), it)  # 构造新的iter

def equal(n):
   return str(n) == str(n)[::-1]

#回文数
def huiwen(x):
    return filter(equal , range(1 , x))
        

def main():
    filterTest()


if __name__ == '__main__':
    main()
