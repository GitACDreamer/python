# 题目：输入某年某月某日，判断这一天是这一年的第几天？
# 闰年需要同时满足以下条件：
# 1、年份能被4整除；
# 2、年份若是 100 的整数倍的话需被400整除，否则是平年。

import time


def countDate(dateString):
     # 获取本年的第一天
    dateStringS = dateString[:4] + '-01-01';

    try:
        # 将string转换成date
        dateS = time.strptime(dateStringS, '%Y-%m-%d')
        dateE = time.strptime(dateString, '%Y-%m-%d')

        # 将date转换成时间戳
        dateMS = time.mktime(dateS)
        dateME = time.mktime(dateE)

        return (dateME - dateMS) / (24 * 3600) + 1
    except Exception as e:
        print(e)
        return -1


def isLeapYear(year):
    if (year % 4 == 0 or year % 400 == 0) and (year % 100 != 0):
        return 1
    else:
        return 0


def countDateth():
    y = int(input('请输入年：'))
    m = int(input('请输入月：'))
    d = int(input('请输入日：'))

    if y <= 0:
        print('输入的年有误!')
        return
    if m <= 0 or m > 12:
        print('输入的月份有误!')
        return
    if d <= 0 or d > 31 or (isLeapYear(y) and m == 2 and d > 29) or (isLeapYear(y) == 0 and m == 2 and d > 28):
        print('输入的日有误!')
        return
    days = [0,31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    day = 0
    for i in range(1,m):
        d += days[i]
    print('这是本年的第%d天.' % (day + isLeapYear(y) + d))


if __name__ == '__main__':
    count = countDate(input('请输入年月日,格式如：2017-06-01   '))
    if count == -1:
        print('输入的日期错误!')
    else:
        print('这是本年的第%d天.' % count)

    countDateth()
