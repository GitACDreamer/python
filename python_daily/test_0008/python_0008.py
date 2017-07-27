'统计一个目录下所有的py代码文件数、总代码行数、空行数、注释行数'

import os
import re
import string

def countCodesNum():
    try:
        total_count_file = 0
        total_count_space = 0
        total_count_code_lines = 0
        total_count_annotation_lines = 0
        filepath = r'E:\Programs\Python\python_daily\test_0008';
        # 列出此目录下所有文件
        for file in os.listdir(filepath):
            # 获取文件的后缀名
            postfix = os.path.splitext(file)[1]
            # 判断后缀名是否是.py
            if postfix.lower() != '.py':
                continue
            with open(filepath + '\\' + file , 'r' , -1 , encoding='utf-8') as f:
                for line in f.readlines():
                    lineCur = line.replace('\n', '').replace(' ', '')
                    if lineCur == '':
                        total_count_space += 1
                    elif lineCur.startswith('#'):
                        total_count_annotation_lines += 1
                    total_count_code_lines += 1
            total_count_file += 1
        print('文件数目：', total_count_file)
        print('代码行数：', total_count_code_lines)
        print('空行数目：', total_count_space)
        print('注释行数：', total_count_annotation_lines)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    countCodesNum()
