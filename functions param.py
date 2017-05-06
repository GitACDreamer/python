# 默认参数一定要用不可变对象，如果是可变对象，程序运行时会有逻辑错误！
# 要注意定义可变参数和关键字参数的语法：
# *args是可变参数，args接收的是一个tuple；
# **kw是关键字参数，kw接收的是一个dict。

def test():
    print('power(5)=', power(5))
    # print('power(5)=', power('5'))
    print('power(2,10)=', power(2, 10))

    # 默认参数测试
    enroll('Micheal', 'Male', city='Tianjin')

    # list作为参数测试
    print(add_end([1, 2, 4]))
    print(add_end([1, 2, 4]))

    print(add_end())
    print(add_end())

    #可变参数
    print(calc(1,3,5,7))
    print(calc(1,2,3,4,5,6,7,8,9,10))

    # Python允许你在list或tuple前面加一个*号，把list或tuple的元素变成可变参数传进去
    param = [2,4,6,8,10]
    print(calc(*param))

    #关键字参数测试
    person('LiMing' , 23)
    person('Liliang' , 25, city ='ShenZhen',job='Engineer')

    extra = {'city': 'HengYang' ,'job' :'Student' , 'zipcode':451525}
    person('LiHua' , 23 , **extra)
    print(extra)

    # 组合参数测试1
    fun1(1,2)
    fun1(1,2,3)
    fun1(1,2,3,4,5,6)
    fun1(1,2,3,4,5,6,**extra)

    # 组合参数测试2
    # fun2(1,2)   missing 1 required keyword-only argument: 'd'
    fun2(1,2,d='d')
    fun2(1,2,d=None)
    fun2(1,2,d=5,**extra)

    args1 = (1,2,3,4,5,6,7,8)
    args2 = (1,2,3)
    kw = {'d':34 ,'x' :'#'}
    fun1(*args1 ,**kw)
    # fun2(*args1 , **kw)  fun2() takes from 2 to 3 positional arguments but 8 positional
                           # arguments (and 1 keyword-only argument) were given
    fun2(*args2 ,**kw)


# pow(x,n) x的n次方
def power(x, n=2):
    if (not isinstance(x, (int, float))) and (not isinstance(n, (int, float))):
        raise TypeError('type error')
    s = 1
    while(n > 0):
        n = n - 1
        s *= x
    return s


def enroll(name, gender, age=6, city='Beijing'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)

# L=[]
# Python函数在定义的时候，默认参数L的值就被计算出来了，即[]，因为默认参数L也是一个变量，它指向对象[]，
# 每次调用该函数，如果改变了L的内容，则下次调用时，默认参数的内容就变了，不再是函数定义时的[]了。
# 所以，定义默认参数要牢记一点：默认参数必须指向不变对象！
def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L

# 可变参数
def calc(*numbers):
    s = 0
    for n in numbers:
        s += n
    return s


# 关键字参数
def person(name ,age , **cy):
    if 'city' in cy:
        print('it has \'city\' arg')
        pass
    if 'job' in cy:
        print('it has \'job\' arg')
    print('name:',name ,'age:',age ,'other:' ,cy)


# 组合参数1
# 在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，
# 这5种参数都可以组合使用。但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数
def fun1(a , b ,c =0 , *arg ,**kw):
    print('a=' ,a ,'b=',b,'c=',c , 'arg=',arg , 'kw=' ,kw)

# 组合参数测试2
# 使用命名关键字参数时，要特别注意，如果没有可变参数，
# 就必须加一个*作为特殊分隔符。如果缺少*，Python解释器将无法识别位置参数和命名关键字参数
def fun2(a,b,c=0,*,d,**kw):
    print('a=' ,a ,'b=',b,'c=',c , 'd=',d , 'kw=' ,kw)


def main():
    test()


if __name__ == '__main__':
    main()
