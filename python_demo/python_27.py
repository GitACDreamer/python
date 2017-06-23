# 题目：利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来。


def showReverse(text, n):
    if n == 0:
        return
    else:
        print(text[n - 1], sep='', end='')
        showReverse(text, n - 1)

if __name__ == '__main__':
    text = input('input a text:')
    showReverse(text, len(text))
