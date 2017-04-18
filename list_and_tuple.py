def main():
    classmates = ['Machael' ,'Bob' ,'July','Tracy'];
    print(classmates)
    print(len(classmates))
    # python的数组索引下标是从0开始,如果下标小于0时，取它的逆序数组的值
    print(classmates[0] ,classmates[1],classmates[2],classmates[3])
    print(classmates[-1] , classmates[-2] , classmates[-3], classmates[-4])
    # 下标越界测试
    # print(classmates[4] , classmates[-5])

    # 数组追加元素
    classmates.append('LiMing')

    # 替换数组中某个元素 
    classmates[1] = 'hello'
    print(classmates);

    # 删除数组中某个元素
    print(classmates.pop(2))
    print(classmates)

    # 数组中的元素可以类型不同
    listOne = ['See' , True , 1234]
    print(listOne)

    # list 元素也可以包含另一个list
    listTwo = ['python' , 'java' , ['asp','php'],'schema' , 'c++']
    print(listTwo)
    print(len(listTwo))
    print(listTwo[1])
    print(listTwo[2])

    # list 为空时
    listNull = [] ;
    print(listNull)

if __name__ == '__main__':
    main()