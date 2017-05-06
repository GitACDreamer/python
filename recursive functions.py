# def fact(n):
#     if not isinstance (n ,(int)):
#         raise TypeError('error type')
#     if n == 1:
#         return 1
#     else:
#         return n*fact(n-1)

# 尾递归优化模式
def fact(n):
    return fact_iter(n, 1)

# 尾递归是指，在函数返回的时候，调用自身本身，并且，return语句不能包含表达式
# Python标准的解释器没有针对尾递归做优化，任何递归函数都存在栈溢出的问题。
def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)
    
def main():
    # n!递归函数
    print('fact(10)=' ,fact(10))
    # print('fact(\'10\')=' ,fact('10'))
    # print('fact(1000)=' , fact(1000)) RecursionError: maximum recursion depth exceeded
    print('fact(100)=' ,fact(100))


if __name__ == '__main__':
    main()