'定制类' 

class Chain(object):
    def __init__(self , path=''):
        self.__path = path
    def __call__(self):
        print('the path is %s' % self.__path)
    def __getattr__(self, path):
        return Chain('%s/%s' %(self.__path , path))
    def __str__(self):
        return self.__path
    __repr__ = __str__

def main():
    call = Chain().status.user.timeline.list
    print(call)
    cc = Chain('root/data/document')
    cc()

    # 判断一个变量是对象函数函数可以通过判断是否可callable
    print(callable(Chain))
    print(callable(max))
    print(callable([1,2,3]))
    print(callable(None))
    print(callable(str))

if __name__ == '__main__':
    main()