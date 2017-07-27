'序列化和反序列化文件'

import pickle
import json


def testWritePickle():
    d = dict(name='Bob', age=20, score=88)
    pickle.dumps(d)

    with open('dump.txt', 'wb') as f:
        pickle.dump(d, f)


def testReadPickle():
    with open('dump.txt', 'rb') as f:
        d = pickle.load(f)
    print(d)


class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score


def dict2Student(d):
    return Student(d['name'], d['age'], d['score'])


def testJson():
    d = dict(name='Bob', age=22, score=82)
    # 序列化为json
    print(json.dumps(d))

    # 解析json
    json_str = '{"name":"july" , "age":20 , "score": 81}'
    d2 = json.loads(json_str)
    print(d2)

    # 解析class
    s = Student('Micheal', 18, 110)
    print(json.dumps(s, default=lambda obj: obj.__dict__))
    s2 = json.loads(json_str, object_hook=dict2Student)
    print(s2.__dict__)


def main():
    testWritePickle()
    testReadPickle()
    testJson()

if __name__ == '__main__':
    main()
