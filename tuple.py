def test():
    # tuple 是有序数组，一旦初始化后不能修改其元素和长度
    classmate= ('Michael','Bob','July')
    print(classmate) ;
    
    # 修改元素测试
    # 出现TypeError: 'tuple' object does not support item assignment
    # classmate[1] = 'Smith'

    # 空的tuple
    tupleNull = ()
    print(tupleNull)

    # tuple 只有一个元素时的定义,需要添加一个逗号来消除歧义
    tupleOne = (1,)
    print(tupleOne)

    # '可变的' tuple ，前提如果里面有其它嵌套的可变元素，只能改变可变的部分
    # tupleTwo[0][0] = 'c' 仍然会报错
    tupleTwo = ('a' ,'b' ,['A' ,'B'])
    print(tupleTwo)
    tupleTwo[2][0] = 'X'
    tupleTwo[2][1] = 'Y'
    print(tupleTwo) 


def main():
    test()


if __name__ == '__main__':
    main()
