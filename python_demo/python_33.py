# 题目：按逗号分隔列表。

if __name__ == '__main__':
    L = [1, 2, 3, 4, 5]
    s1 = ','.join(str(n) for n in L)
    print(s1)
