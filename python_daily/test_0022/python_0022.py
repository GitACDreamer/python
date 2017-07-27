# coding=utf-8
# @author: Leland
# @email:  AC_Dreamer@163.com
# @date:   2017-07-26 09:52:16
# @title:  resize the image


import os
from PIL import Image


def transfer(image_path, dest_width, dest_height, dest_path):
    im = Image.open(image_path)
    w, h = im.size
    if dest_width / w < dest_height / h:
        ratio = dest_width / w
    else:
        ratio = dest_height / h
    resized_img = im.resize((int(ratio * w), int(ratio * h)), Image.ANTIALIAS)
    resized_img.save(dest_path)


if __name__ == '__main__':
    try:
        filepath = r'E:\Programs\Python\python_daily\test_0022';
        files = os.listdir(filepath)
        for file in files:
            # 获取文件的后缀名
            postfix = os.path.splitext(file)[1]  # 筛选出此目录下所有的图片
            if(postfix.lower() == '.py'):
                continue
            transfer(filepath + "\\" + file, 1136,
                     640, filepath + "\\5_" + file)
            transfer(filepath + "\\" + file, 1334,
                     750, filepath + "\\6_" + file)
            transfer(filepath + "\\" + file, 2200,
                     1242, filepath + "\\6+_" + file)
    except Exception as e:
        print(e)
