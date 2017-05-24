'枚举类的使用'

from enum import Enum, unique

@unique
class Weekday(Enum):
    Sunday = 0
    Monday = 1
    Tuesday = 2
    Wednesday = 3
    Thursday = 4
    Firday = 5
    Saturday = 6

@unique
class Month(Enum):
    January = 1
    February = 2
    Marcy = 3
    April = 4
    May = 5
    June = 6
    July = 7
    August = 8
    September = 9
    October = 10
    November = 11
    December = 12
def print_values(object):
    for name , member in object.__members__.items():
        print(name , '=>' ,member , ',' , member.value)
def main():
    print_values(Weekday)
    print_values(Month)

if __name__ == '__main__':
    main()
