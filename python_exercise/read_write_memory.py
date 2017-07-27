'内存读写' 

# StringIO操作的只能是str，如果需要操作二进制数据，就需要使用BytesIO

from io import StringIO
from io import BytesIO

def read_write_memory():
    f1 = StringIO()
    f1.write('hello')
    f1.write(',')
    f1.write('world')
    print(f1.getvalue())
    f1.close()

    f2 = StringIO('Hello!\nHi\nGoodbye!')
    while True:
        s = f2.readline()
        if s == '':
            break
        print(s.strip())
    f2.close()

    f3 = BytesIO()
    f3.write('中文'.encode('utf-8'))
    print(f3.getvalue())
    f3.close()

    f4 = BytesIO(b'\xe4\xb8\xad\xa6\x96\x87')
    print(f4.read())
    f4.close()

def main():
    read_write_memory()

if __name__ == '__main__':
    main()