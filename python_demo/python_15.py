# 题目：利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间的用B表示，
# 60分以下的用C表示。
# 程序分析：程序分析：(a>b)?a:b这是条件运算符的基本例子。


def score():
    score = int(input('请输入分数：'))
    if score >= 90:
        print('A')
    elif score >= 60:
        print('B')
    else:
        print('C')

if __name__ == '__main__':
    score()
