def sortTest():
    L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

    # 按姓名排序
    print(sorted(L, key=by_name))

    # 按分数排序(逆序)
    print(sorted(L, key=by_score, reverse=True))

    d = {'Sily': 45, 'Eda': 78, 'admin': 23, 'Queue': 98, 'zip': 66}

    # 按key排序(不区分大小写)
    print(sorted(d.items(), key=lambda d: d[0].lower()))

    # 按value排序
    print(sorted(d.items(), key=lambda d: d[1]))


def by_name(t):
    return t[0]


def by_score(t):
    return t[1]


def main():
    sortTest()


if __name__ == '__main__':
    main()
