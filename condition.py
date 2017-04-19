def test():
    # 条件判断
    age = 11
    if age >= 18:
        print('you age is', age)
        print('adult')
    elif age >= 6:
        print('teenage')
    else:
        print('you age is', age)
        print('kid')
    # Python 语法与缩进的距离有关系 ，条件语句一定要缩放，不然会有语法错误
    print('if else外面')

    # 语法格式
    # if <条件判断1>:
    #    <执行1>
    # elif <条件判断2>:
    #    <执行2>
    # elif <条件判断3>:
    #    <执行3>
    # else:
    #     <执行4>

    # 输入条件
    birth = int(input('input the birth of year: '))
    if birth < 2000:
        print('00前')
    else:
        print('00后')


def BMI():
    hight = float(input('请输入身高 例如：1.75  '))
    weight = float(input('请输入体重 例如：80.5  '))
    bmi = weight / (hight * hight)
    if bmi < 18.5:
        print('过轻')
    elif bmi >= 18.5 and bmi < 25:
        print('正常')
    elif bmi >= 25 and bmi < 28:
        print('过重')
    elif bmi >= 28 and bmi < 32:
        print('肥胖')
    elif bmi >= 32:
        print('严重肥胖')
    print('bmi=', bmi)


def main():
    test()
    BMI()


if __name__ == '__main__':
    main()
