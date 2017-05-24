'使用元类'

# 要创建一个class对象，type()函数依次传入3个参数：
# 1. class的名称；
# 2. 继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
# 3. class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hi上。
class Hello(object):
    def hello(self, name='world'):
        print('Hello,%s' % name)


def fn(self, name='Bob'):
    print('Hello , %s' % name)


# metaclass是类的模板，必须要从type类型派生
# __new__()方法接收到的参数依次是：
# 1.当前准备创建的类的对象；
# 2.类的名字；
# 3.类继承的父类集合；
# 4.类的方法集合。
class ListMetaclass(type):
    def __new__(mcs, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(mcs, name, bases, attrs)

class NewList(list, metaclass=ListMetaclass):
    pass

# metaclass是类的模板，所以必须从`type`类型派生：
class ListMetaclass2(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)
class MyList(list, metaclass=ListMetaclass2):
    pass

def main():

    # 显示类型
    print(type(Hello))
    h = Hello()
    print(type(h))

    # 使用type创建类
    Hi = type('Hi', (object,), dict(hi=fn))  # 创建Hi class
    h2 = Hi()
    h2.hi()
    print(type(Hi))
    print(type(h2))

    # metaclass
    L = NewList()
    L.append(1)
    L.append(2)
    print(L)

if __name__ == '__main__':
    main()
