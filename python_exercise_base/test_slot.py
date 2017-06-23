'给类绑定方法和属性'
# 给一个实例绑定的方法和属性，对另一个实例是不起作用的：

from types import MethodType

class Student(object):
    __slots__ = ('age' , 'gender') 
    
def set_gender(self , gender='F'):
    self.gender = gender 
def get_gender(self):
    return self.gender

def testSlot():
    s = Student()
    s.age = 20 
    #s.score = 89 Assigning to attribute 'score' not defined in class slots
    Student.set_gender = set_gender
    Student.get_gender = get_gender
    s.set_gender('F')
    print(s.get_gender())
    s2 = Student()
    s2.set_gender()
    print(s2.get_gender())
def main():
    testSlot()

if __name__ == '__main__':
    main()