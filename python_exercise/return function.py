# 当我们调用lazy_sum()时，每次调用都会返回一个新的函数,也就是说每次返回的对象都是new的，所以测试
# 样例中f1 == f2 为false


def lazy_sum(*arg):

    def sum():
        s = 0
        for x in arg:
            s += x
        return s
    return sum

# 全部都是9.原因就在于返回的函数引用了变量i，但它并非立刻执行。
# 等到3个函数都返回时，它们所引用的变量i已经变成了3，因此最终结果为9。
# 所以，返回函数不要引用任何循环变量，或者后续会发生变化的变量

def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i
        fs.append(f)
    return fs


def main():

    # lazy_sum
    f1 = lazy_sum(*list(range(1, 10)))
    f2 = lazy_sum(*list(range(1, 10)))
    print(f1())
    print(f2())
    print(f1 == f2)

    # count
    fn= count()
    print(fn[0](),fn[1](),fn[2]())

    # 匿名函数
    # 名函数有个限制，就是只能有一个表达式，不用写return，返回值就是该表达式的结果
    L = list(map(lambda x: x*x*x , list(range(1,11))))
    print(L)

if __name__ == '__main__':
    main()
