def test():
    # dict test
    d = {'Michael': 22, 'Lisa': 44, 'July': 55}
    print(d)

    # 根据key，找到value
    # 先判断key是否存在,如果存在则打印value
    if 'Lisa' in d:
        print(d['Lisa'])

    # 判断key是否存在方法2,如果存在则打印value,否则打印Null
    print(d.get('Liss'))

    # 删除一个key，其value也会随之删除
    if d.get('July'):
        print(d.pop('July'))
    print(d)

    # dict 和 list的区别
    # dict
    # 1. 查找和插入的速度极快，不会随着key的增加而增加
    # 2. 需要占用大量的内存，内存浪费多
    # list
    # 1. 查找和插入的时间随着元素的增加而增加
    # 2. 占用的空间小，浪费的内存少
    # dict的key是不可变的，同样的key多次赋值，则会覆盖原有的值

    d['Michael'] = 200
    print(d)

    print(d.pop('Michael'))
    print(d)

    set1 = set([1, 2, 4, 5, 3, 2, 1, 0])
    set2 = set([1, 3, 5, 7])
    print(set1)
    print(set2)
    print('set1 & set2 =', set1 & set2)
    print('set1 | set2=', set1 | set2)
    print('set1 ^ set2=', set1 ^ set2)
    
    set1.remove(1)
    print(set1)


def main():
    test()


if __name__ == '__main__':
    main()
