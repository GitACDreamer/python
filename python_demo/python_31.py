# 题目：请输入星期几的第一个字母来判断一下是星期几，如果第一个字母一样，则继续判断第二个字母。
import re

def WhatDay():
    week = ['Sunday', 'Monday', 'Tuesday',  'Wednesday',
            'Thursday', 'Friday', 'Saturday']
    print('每次输入一个首字母查找星期几^_^')
    letters = ''
    while True:
        letter = input('请输入字母：')
        letters += letter
        #letter = 'S'
        result = []
        for w in week:
            if re.match(letters.lower(), w.lower(),):
                result.append(w)
        if len(result) == 0:
            print('你的输入有误！')
            break
        elif len(result) == 1:
            print(result[0])
            break


if __name__ == '__main__':
    WhatDay()
