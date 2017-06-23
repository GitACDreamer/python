# 题目：给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字。


def showReverse(text):
    print(len(text))
    print(text[::-1])


if __name__ == '__main__':
    while True:
        showReverse(input('请输入数字'))
