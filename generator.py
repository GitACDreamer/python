# generator和函数的执行流程不一样。函数是顺序执行，遇到return语句或者最后一行函数语句就返回。而变成generator的函数，
# 在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行
def generator():
    # 生成器存储1~10的平方的算法
    g = (x*x for x in range(11))
    for n in g:
        print(n)
    # 斐波拉契数列
    g = fibonacci(6)
    print(g)  # g is a generator
    for n in fibonacci(6):
        print(n)

    for t in triangles(10):
        print(t)

def fibonacci(max):
    n,a,b = 0,0,1
    while n < max:
        yield b
        a,b = b , a+b
        n = n+1
    return 'done'


def triangles(n): 
    L=[1]
    for x in range(n):
        yield L;
        L=[1]+ [L[i]+L[i+1] for i in range(x)] +[1]

def main():
    generator()


if __name__ == '__main__':
    main()
