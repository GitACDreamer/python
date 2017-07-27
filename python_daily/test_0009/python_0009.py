' 一个HTML文件，找出里面的正文'

import re
import os
from bs4 import BeautifulSoup 

def find_html_body():
    try:
        filepath = r'E:\Programs\Python\python_daily\test_0009\p0009.html'
        with open(filepath, 'r', -1, encoding='utf8') as f:
            body = ''
            isbody = False
            for line in f.readlines():
                if re.match(r'<body>', line):
                    isbody = True
                if isbody:
                    body += line
                if re.match(r'</body>', line):
                    break
            print(body)
    except Exception as e:
        print(e)

def find_the_body():
    try:
        with open(r'E:\Programs\Python\python_daily\test_0009\p0009.html' , 'r' , -1 , encoding='utf8') as f:
            text = BeautifulSoup(f , 'html.parser')
            content = text.get_text().strip('\n')
            print(content)
    except Exception as e:
        print(e)

if __name__ == '__main__':
    # find_html_body()
    find_the_body()
