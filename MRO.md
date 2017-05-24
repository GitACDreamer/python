# MRO的计算

```merge```的计算规则如下
> take the head of the first list, i.e L[B1][0]; if this head is not in the tail of any of the other lists,
then add it to the linearization of C and remove it from the lists in the merge, otherwise look at the 
head of the next list and take it, if it is a good head. Then repeat the operation until all the class 
are removed or it is impossible to find good heads. In this case,it is impossible to construct the merge,
Python 2.3 will refuse to create the class C and will raise an exception.

## 1.先从简单的类开始
```
class B(object): pass
L[B] = L[B(object)]
     = B + merge(L[object])
     = B + L[object]
     = B + object
B.__mro__ = (<class '__main__.B'> , <type 'object'>)
```

## 2. 简单子类
```
class C(B): pass
L[C] = L[C(B)]
     = C + L[B]   # 从1已经得到L[B] = B object
     = C B object
C.__mro__ = (<class '__main__.C'> , <class '__main__.B'>,<type , 'object'>)
```

## 3. 复杂的例子
```
O = object
class F(O): pass
class E(O): pass
class D(O): pass
class C(D,F): pass
class B(D,E): pass
class A(B,C): pass

L[O] = O = object
L[F] = F O
L[E] = E O
L[D] = D O
L[C] = L[C(D,F)]
     = C + merge(L[D], L[F] , DF)
     # 从前面知道L[D],L[F]的值
     = C + merge(DO , FO ,DF)
     # 因为D是顺序第一个并且在包含几个D的list中都是head,
     # 所以这次去D同时将列表中的D删除
     = C + D + merge(O , FO , F)
     # 因为O虽然在第一个是heade，但是其它的list(FO)并不是head,所以跳过
     # 改为检查第二个list(FO),F是所有含F的list列表中的头，所以取F,同时
     # 删除F
     = C + D + F + merge(O)
     = C D F O
C.__mro__ = (<class '__main__.C'>,<class '__main__.D'>,<class '__main__.F'>,<type ,'object'>)
```

```
L[B] = L[B(D,E)]
     = B + merge(L[D] , L[E] , DE)
     = B + merge(DO , EO , DE)
     = B + D + merge(O , EO , E)
     = B + D + E + merge(O)
     = B D E O
B.__mro__ = (<class '__main__.B'>,<class '__main__.D'>,<class '__main__.E'>,<type ,'object'>)
```

```
L[A] = L[A(B ,C)]
     = A + merge(L[B] , L[C] , BC)
     = A + merge(BDEO , CDFO , BC)
     = A + B + merge(DEO , CDFO , C)
     = A + B + C + merge(DEO , DFO)
     = A + B + C + D + merge(EO , FO)
     = A + B + C + D + E + F + merge(O)
     = A B C D E F O
A.__mro__ = (<class '__main__.A'>,<class '__main__.B'>,<class '__main__.C'>,
<class '__main__.D'>,<class '__main__.E'>,<class '__main__.F'>,<type ,'object'>)
```