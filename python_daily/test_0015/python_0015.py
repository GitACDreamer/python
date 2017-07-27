# coding=utf-8
# @Author:  Leland
# @Date:    2017-07-13 18:21:02
# @Funtion: 将txt文件内容写到xls里面去

import os
import json
import xlwt


def read_text(path):
    """将txt文本转换成json"""
    try:
        with open(path, 'r', buffering=-1, encoding='utf-8') as f:
            text = f.read()
            text_json = json.loads(text)
        return text_json
    except IOError as e:
        print(e)


def save_into_excel(content_dict, excel_name):
    """将json数据写到excel里面"""
    wb = xlwt.Workbook()
    ws = wb.add_sheet('student', cell_overwrite_ok=True)
    row, col = 0, 0

    if isinstance(content_dict, dict):
        for k, v in sorted(content_dict.items(), key=lambda d: d[0]):
            ws.write(row, col, k)
            if isinstance(v, list):
                for i in v:
                    col += 1
                    ws.write(row, col, i)
            elif isinstance(v, str):
                col += 1
                ws.write(row, col, v)
            row += 1
            col = 0
    elif isinstance(content_dict, list):
        for a in content_dict:
            # 元素是list
            if isinstance(a, list):
                for b in a:
                    ws.write(row, col, b)
                    col += 1
            else:
                ws.write(row, col, a)
            row += 1
            col = 0
    wb.save(excel_name)


if __name__ == '__main__':
    # json_text = read_text(os.path.join(
    #     os.path.split(__file__)[0], 'student.txt'))
    # save_into_excel(json_text, 'student.xls')
    # json_city = read_text(os.path.join(os.path.split(__file__)[0], 'city.txt'))
    # save_into_excel(json_city, 'city.xls')
    json_city = read_text(os.path.join(
        os.path.split(__file__)[0], 'number.txt'))
    save_into_excel(json_city, 'number.xls')
