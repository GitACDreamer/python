# coding=utf-8
# @Author:  Leland
# @Date:    2017-07-13 17:20:22
# @Funtion: 第 0013 题： 用 Python 写一个爬图片的程序，爬 这个链接里的图片

import os
from urllib import request
from bs4 import BeautifulSoup


def crawl_image():
    try:
        file = request.urlopen('https://tieba.baidu.com/p/5219398194').read()
        soup = BeautifulSoup(file, "html.parser")
        images = soup.find_all('img', {"class": "BDE_Image"})
        count = 1
        # 创建目录
        os.makedirs(r'E:\Programs\Python\python_daily\test_0014',
                    mode=0o777, exist_ok=True)
        # 遍历保存图片
        for image in images:
            filename = r'E:\Programs\Python\python_daily\test_0014' + \
                r'\p00' + str(count) + '.jpg'
            content = request.urlopen(image['src']).read()
            with open(filename, 'wb') as f:
                f.write(content)
            count += 1
    except Exception as e:
        print(e)


if __name__ == '__main__':
    crawl_image()
