import functools

def log(text):
    def decorator(func):
        # 需要把原始函数的__name__等属性复制到wrapper()函数中
        @functools.wraps(func) 
        def wrapper(*args , **kw):
            print('%s %s():' %(text ,func.__name__))
            return func(*args , **kw)
        return wrapper
    return decorator

@log('excute')
def now():
    print('2017.05.16')
        
def decoratorTest():
    now()
    print(now.__name__)

def main():
    decoratorTest()

if __name__ == '__main__':
    main()