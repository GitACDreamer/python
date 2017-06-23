# 打印菱形


def printRhombus():
    space = 3
    pic = 1
    for i in range(4):
        # 打印空格
        for j in range(space):
            print(' ', sep='', end='')
        # 打印星号
        for j in range(pic):
            print('*', sep='', end='')
        # 打印空格
        for j in range(space):
            print(' ', sep='', end='')
        print('')
        pic += 2
        space -= 1
    space = 1
    pic = 5
    for i in range(3):
        # 打印空格
        for j in range(space):
            print(' ', sep='', end='')
        # 打印星号
        for j in range(pic):
            print('*', sep='', end='')
        # 打印空格
        for j in range(space):
            print(' ', sep='', end='')
        print('')
        pic -= 2
        space += 1


if __name__ == '__main__':
    printRhombus()
