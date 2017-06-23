import functools

def partialTest():
    maxNew = functools.partial(max , 5)
    print(maxNew(1,2,-1,3))

def main():
    partialTest()

if __name__ == '__main__':
    main()