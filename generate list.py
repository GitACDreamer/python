import os

def generateList():
    # 取1~10的数
    L1 = list(range(1,11))
    print(L1)
    # 取1~100的奇数
    L2 = list(range(1,100,2))
    print(L2)
    # 取1~10的数的平方
    L3 = [x*x for x in range(1,11)]
    print(L3)
    # 1~10中取偶数的平方
    L4 = [x*x for x in range(1,11) if x%2 ==0]
    print(L4)
    # 生成全排列
    L5= [m+n for m in 'ABC' for n in 'XYZ']
    print(L5)

    # 列出当前目录所有文件和目录
    L6 = [d for d in os.listdir('.')]   # os.listdir可以列出文件和目录
    print(L6)

    # dict 迭代key 和 value
    L7 = {'x':'A' ,'y':'B','z':'C','m':'D'}
    for k , v in L7.items():
        print(k,'=',v)

    # 将list列表中所有的大写字母变小写,非字符串不用转换
    L8 = ['Lisa' , 'Micheal' , 8,'A','Tracy' , 'Bob' , 'Tom' , '' , None]
    print(L8)
    L9 = [s.lower() for s in L8 if isinstance(s , (str)) ]
    print(L9)

def main():
    generateList()

if __name__ == '__main__':
    main()