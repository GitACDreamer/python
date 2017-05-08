from collections import Iterable

# 任何可迭代对象都可以作用于for循环，包括我们自定义的数据类型，只要符合迭代条件，就可以使用for循环。
def iterator():
    dictionary = {'a': 1, 'b': 3, 'c': 3, 'd': 4, 'e': 5}
    for k, v in dictionary.items():
        print('key->value=', k, ':', v)

    A = 'ABCDEFGHIJKL'
    for a in A:
        print(a)

    # 判断是否可迭代
    print('\'1234\'是否可迭代', isinstance('1234', Iterable))
    print('[\'1\',\'2\',\'3\',\'4\']是否可迭代',
          isinstance(['1', '2', '3', '4'], Iterable))
    print('123是否可迭代', isinstance(123, Iterable))

    # 下标方式访问
    for i, value in enumerate(A):
        print(i, value)

    coord = [(1, 1), (2, 3), (4, 5), (5, 8), (8, 7), (9, 2)]
    for x, y in coord:
        print(x, y)


def main():
    iterator()


if __name__ == '__main__':
    main()
