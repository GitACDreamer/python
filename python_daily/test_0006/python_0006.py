# 调整某个目录下所有图片的大小为指定的尺寸

from PIL import Image
import os
import re


def resizeDirectoryImage(w,h):
    try:
        filepath = r'E:\Programs\Python\python_daily\test_0006'
        files = os.listdir(filepath)
        for file in files:
            im = Image.open(filepath + '\\' + file)
            im.resize((w,h))
            postfix = os.path.splitext(file)[1][1:]
            im.save(filepath + '\\' + file, postfix)
    except Exception as e:
        print(e)

if __name__ == '__main__':
    resizeDirectoryImage(100,100)
