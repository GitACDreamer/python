#--*utf-8*--

'面向对象编程'

__author__ = 'Leland'

class Student(object):
    def __init__(self , name , score , age):
        self.__name = name
        self.__score = score
        self.__age = age
    def print_student_info(self):
        print(self.__name ,':' ,self.__score , ':' , self.__age)
    def get_name(self):
        return self.__name
    def set_name(self , name):
        self.__name = name 

def main():
    july = Student('July Mute' , 82 , 21)
    july.print_student_info()
    tom = Student('Tom DongHong' , 67 ,22)
    tom.print_student_info()
    print(july)
    print(Student)
    # Python允许对实例变量绑定任何数据，也就是说，对于两个实例变量，
    # 虽然它们都是同一个类的不同实例，但拥有的变量名称都可能不同
    july.gender = 'F'
    print(july.gender)
    # print(tom.gender) AttributeError: 'Student' object has no attribute 'gender'
    july.print_student_info() # 此时的Student类有gender属性
    tom.print_student_info()  # Student类没有gender属性

    july.score = 100
    print(july.get_name())
    july.set_name(july.get_name() + ' new')
    july.print_student_info()

if __name__ == '__main__':
    main()