'继承与多态性和测试对象的属性'


# 继承与多态的“开闭原则”
# 对扩展开放：允许新增Animal子类；
# 对修改封闭：不需要修改依赖Animal类型的run_twice()等函数。

class Animal(object):
    def run(self):
        print('Animal is running')
    
class Dog(Animal):
    def run(self):
        print('Dog is running')

class Cat(Animal):
    def run(self):
        print('Cat is running')

class Tortoise(Animal):
    def run(self):
        print('Tortoise is running slowly')

# 动态语言的鸭子类型特点决定了继承不像静态语言那样是必须的。
# 对于静态语言（例如Java）来说，如果需要传入Animal类型，则传入的对象必须是Animal类型或者它的子类，否则，将无法调用run()方法。
# 对于Python这样的动态语言来说，则不一定需要传入Animal类型。我们只需要保证传入的对象有一个run()方法就可以了

class Timer(object):
    def run(self):
        print('Start……')
    
def run_twice(animal):
    animal.run()
    animal.run()

class newObject(object):
    base = 10
    def __init__(self):
        self.x = 9
    def power(self):
         return self.x*self.x

def main():
    # dog
    dog = Dog() 
    dog.run() 

    # cat 
    cat = Cat()
    cat.run()

    # object type test
    a = list()   # a is a list type
    animal = Animal() # animal is a Animal type
    dog = Dog()       # dog is a Animal and Dog type
    print(isinstance(a , list))       # True
    print(isinstance(animal ,Animal)) # True
    print(isinstance(dog , Animal))   # True
    print(isinstance(dog , Dog))      # True
    print(isinstance(animal , Dog))   # False
    print(isinstance(a , (list , tuple))) # True
    # 获取一个对象的所有属性和方法
    a = 'ABC'
    print(dir(a))
    bb = a.replace('AB' ,'CDEE')
    print(bb)
    print(bb.startswith('C'))

    # polymorphism
    run_twice(Animal())
    run_twice(Dog())
    run_twice(Cat())
    run_twice(Tortoise())

    # 鸭子类型（python继承）
    run_twice(Timer())

    # 测试对象的属性
    obj = newObject()

    # 列出所有属性和方法
    print(dir(object))
    
    # 有x属性吗？
    print(hasattr(obj , 'x'))  
    print(obj.x)

    # 有y属性吗？
    print(hasattr(obj , 'y'))
    # 设置y属性
    setattr(obj , 'y' , 20)
    print(hasattr(obj , 'y'))
    #获取y属性
    print(getattr(obj , 'y'))
    print(obj.y)

    # 获取z属性
    print(getattr(obj , 'z' ,404))

    # 有power属性吗？
    print(hasattr(obj , 'power'))
    print(getattr(obj , 'power'))
    print(getattr(obj , 'power')())

    # 类属性和实例属性
    ob1 = newObject()
    ob2 = newObject()
    print(ob1.base)
    ob2.base = 11 
    print(ob2.base)
    print(ob1.base)
    print(newObject.base)
    newObject.base = 20
    print(ob1.base)
    print(ob2.base)
    del ob2.base
    print(ob2.base)
    # del newObject.base
    # print(ob1.base) AttributeError: 'newObject' object has no attribute 'base'

if __name__ == '__main__':
    main()