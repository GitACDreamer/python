def main():
    print('10+20 =', 10 + 20)
    print('Hello,World')
    name = input('please enter your name: ')
    # 输入用户名
    print('my name is', name)
    print(r'\'')
    # 转义
    print('\\n\\')
    print(r'\\n\\')
    print(r'\t')
    print(r'\t\t')
    print('''line1
line2
line3''')
    print(3 > 2)
    print(3 < 2)
    print(5 > 3 and 3 > 1)
    print(5 > 3 or 3 < 1)
    print(not 1 > 2)
    print(None)
    # 声明变量无需指定类型，它自己会判断
    age = 12
    if age >= 18:
        print('adult')
    else:
        print('teenager')
    # 同一个变量可以重复赋值
    age = 'ABC'
    print(age)


if __name__ == '__main__':
    main()
