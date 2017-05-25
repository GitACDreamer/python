'查找文件'

import os

def findFile(dir=os.curdir, key='py'):
    adirs = []
    for root, folders, files in os.walk(dir):
        for file in files:
            tFile = file.partition('.')[0]
            if key in tFile:
                adirs.append(os.path.relpath(os.path.join(root, file), dir))
    print('Current direction: %s' % os.path.abspath(dir))
    print('Find Files: %s' % adirs)

def main():
    findFile('E:\\Programs\\', 'special')


if __name__ == '__main__':
    main()
