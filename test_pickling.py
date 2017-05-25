'序列化和反序列化文件'

import pickle


def testWritePickle():
    d = dict(name='Bob', age=20, score=88)
    pickle.dumps(d)

    with open('dump.txt', 'wb') as f:
        pickle.dump(d, f)

def testReadPickle():
    with open('dump.txt' , 'rb') as f:
        d = pickle.load(f)
    print(d)

def main():
    testWritePickle()
    testReadPickle()


if __name__ == '__main__':
    main()
