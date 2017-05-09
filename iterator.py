from collections import Iterator

# 总结
# 这是因为Python的Iterator对象表示的是一个数据流，Iterator对象可以被next()函数调用并不断返回下一个数据，
# 直到没有数据时抛出StopIteration错误。可以把这个数据流看做是一个有序序列，但我们却不能提前知道序列的长度，
# 只能不断通过next()函数实现按需计算下一个数据，
# 所以Iterator的计算是惰性的，只有在需要返回下一个数据时它才会计算。
# Iterator甚至可以表示一个无限大的数据流，例如全体自然数。而使用list是永远不可能存储全体自然数的。
# 凡是可作用于for循环的对象都是Iterable类型；
# 凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；
# 集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象。

def iterator():
    
    # 生成器都是Iterator对象，但list、dict、str虽然是Iterable，却不是Iterator
    # 判断object是否是可迭代对象
    L1 = (x*x for x in range(11))
    print(isinstance(L1 , Iterator))
    print(isinstance([] ,Iterator))
    print(isinstance({} , Iterator))
    print(isinstance('abc' , Iterator))

    # 转换成iterator对象
    print(isinstance(iter([]) , Iterator)) 
    print(isinstance(iter('abc') , Iterator))

    # Python的for循环本质上就是通过不断调用next()函数实现的
    for x in [1,2,3,4,5]:
        print(x)
    
    # 等价于
    it = iter([1,2,3,4,5])
    while True:
        try:
            # 获取下一个值
            x = next(it)
            print(x)
        except StopIteration:
            # 遇到StopIteration退出循环
            break
    

def main():
    iterator()

if __name__ == '__main__':
    main()