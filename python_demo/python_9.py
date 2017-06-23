# 题目：暂停一秒输出。

import time
def sleepShow():
    L=[]
    L = [ i*i for i in range(1,10)]
    for v in L:
        time.sleep(1)
        print(v)

if __name__ == '__main__':
    sleepShow()