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
    age = int(input('请输入你的年龄：'))
    if age >= 18:
        print('adult')
    else:
        print('teenager')
    # 同一个变量可以重复赋值
    age = 'ABC'
    print(age)
    a = 'ABC'
    b = a
    a = 'XYZ'
    print(a)
    print(b)
    PI = 3.1415926
    print(PI)
    print(10 / 3)
    print(9 / 3)
    # 得到结果后，向下取整
    print(10 // 3)
    # 取余
    print(10 % 3)

    # 练习
    n = 123
    f = 456.789
    s1 = 'Hello, world'
    s2 = 'Hello, \'Adam\''
    s3 = r'Hello, "Bart"'
    s4 = r'''Hello,
Lisa!'''

    print(n)
    print(f)
    print(s1,s2,s3,s4)


if __name__ == '__main__':
    main()
