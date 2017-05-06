def test():
    # 循环测试
    names = ['LiMing', 'HuXiao', 'FeiYang', 'XiaoHong']
    for name in names:
        print(name)


def sum():
    # 对1~100求和
    sum = 0
    for x in range(101):
        sum += x
    print(sum)

def oddSum():
    # 对1~100以内的奇数求和
    sum = 0
    n = 99
    while n > 0:
        sum += n
        n -=2
    print(sum)

# 死循环测试，可以按Ctrl+C强制退出程序
# def whileForever():
#    n = 1
#    while n>0:
#        print('Hello')

def main():
    test()
    sum()
    oddSum()
#    whileForever()


if __name__ == '__main__':
    main()
