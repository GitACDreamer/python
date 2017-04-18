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
    print('r\t\t')
    print('''line1
line2
line3''')


if __name__ == '__main__':
    main()
