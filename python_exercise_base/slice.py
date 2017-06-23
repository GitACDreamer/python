def slice():
    L = ['Michael' , 'Sarch', 'Tracy' ,'Bob','Jack']

    # 取前3个数
    n = 3 
    s= [] 
    for i in range(n):
        s.append(L[i])
    print(s)

    #取前3个数
    print(L[:3])

    #取1~3的值
    print(L[1:3])

    #取倒数两个数
    print(L[-2:])
        
    S = list(range(100))
    print(S)

    #取前10个数
    print(S[:10])

    #取30到40的数
    print(S[30:40])

    #取最后10个数
    print(S[-10:])

    #前20个数，每两个取一个
    print(S[:20:2])

    #所有数，每5个取一个数
    print(S[::5])

    #取全部的数
    print(S[:])

    #字符串切片
    STR = 'ABCDEFG'

    #取前3个数
    print(STR[:3])

    #每2隔个数取一个
    print(STR[::2])

    #取最后两个数
    print(STR[-2:])

    #逆序
    print(STR[::-1])

def main():
    slice()

if __name__ == '__main__':
    main()