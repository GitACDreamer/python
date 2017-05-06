# 汉若塔(移动次数2^n -1)
def hanoiTower(n , a , b, c):
    if n == 1:
        #只有一个时，直接A移动到C
        print(a , '----->' , c) 
    else:
        #将n-1个盘子从A移动到B
        hanoiTower(n-1 , a , c , b)
        #将最底下那个盘子从A移动到C
        hanoiTower(1 , a , b ,c)
        #将n-1个盘子从B移动到C
        hanoiTower(n-1 , b , a , c)
        
def main():
    hanoiTower(5 , 'A', 'B','C')

if __name__ == '__main__':
    main()