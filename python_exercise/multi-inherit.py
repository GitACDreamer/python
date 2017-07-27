'多继承的使用' 
# 经典类深度优先，新式类广度优先。换句话来讲就是，经典类是纵向查找，新式类是横向查找。 先入为主原则，先找到谁就听谁的。

class A(object):
    def print_out(self):
        print('A class called')

class B(object):
    def print_out(self):
        print('B class called')

class C(A,B):
   pass
    
class D(B,A):
    pass
    
class E(C):
    pass

class F(D):
    pass

def main():
    a = A() 
    a.print_out()
    b = B()
    b.print_out()
    c = C()
    c.print_out()
    d = D() 
    d.print_out()
    e = E()
    e.print_out()
    f = F()
    f.print_out()

if __name__ == '__main__':
    main()
    