# encoding = utf-8
'查找html里面的连接'

__author__ = 'Leland'

import requests
import re
from bs4 import BeautifulSoup


def find_href():
    try:
        url = input('请输入连接:')
        html = requests.get(url)
        soup = BeautifulSoup(html.text, "html.parser")
        for x in soup.findAll('a'):
            print(x['href'])
    except Exception as e:
        print(e)

if __name__ == '__main__':
    find_href()
