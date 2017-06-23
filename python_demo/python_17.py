# 题目：输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。


def countCharacter(text):
    character = 0
    num = 0
    space = 0
    other = 0
    for ch in text:
        if ch.isalpha():
            character += 1
        elif ch.isnumeric():
            num += 1
        elif ch.isspace():
            space += 1
        else:
            other += 1
    print('字符：%d个、数字：%d个、空格：%d个、其它：%d个' % (character, num, space, other))


if __name__ == '__main__':
    countCharacter(input('请输入一行文字：'))
