import os
import shutil

def test():
    print(os.name)
    print(os.environ)

    # 查看当前目录的绝对路径
    print(os.path.abspath('.'))
    # 在某个目录下创建一个新目录
    os.path.join('E:\\Programs\\Python', 'testdir')
    # 文件夹存在时不能重复创建
    # os.mkdir('E:\\Programs\\Python\\testdir')
    # os.rmdir('testdir')
    print(os.path.split('E:\\Programs\\Python\\test_file.txt'))

    # 列出当前目录下所有的文件夹
    print([x for x in os.listdir('.') if os.path.isdir(x)])

    # 列出当前目录下所有的.py文件
    print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py'])

    shutil.copyfile('E:\\Programs\\Python\\test_file.txt' , 'test_file_copy.txt')

def main():
    test()

if __name__ == '__main__':
    main()
