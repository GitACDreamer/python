# 题目：一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同。

def isPalindromeNum(text):
    if not text.isnumeric():
        return False
    if text == text[::-1]:
        return True
    else:
        return False


if __name__ == '__main__':
    while True:
        num = input('请输入一个数字：')
        if isPalindromeNum(num):
            print('是回文数')
        else:
            print('不是回文数')
