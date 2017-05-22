#--*utf-8*--

'a add function module'

__author__ = 'Leland'

def addFunc(x = 0 , y = 0):
    return x+y 

if __name__ == '__main__':
    print('x+y=' , addFunc(1+1))