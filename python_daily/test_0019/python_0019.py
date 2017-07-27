# coding=utf-8
# @author: Leland
# @email:  AC_Dreamer@163.com
# @date:   2017-07-23 12:45:17
# @title:  将xls转换成xml

import os
import xlrd
import json
from lxml import etree


def read_from_excel(filename):
    xls = xlrd.open_workbook(filename)
    sheet = xls.sheet_by_name('number')
    data = []
    for i in range(sheet.nrows):
        cols = []
        for j in range(sheet.ncols):
            cols.append(sheet.cell_value(i, j))
        data.append(cols)
    return json.dumps(data, ensure_ascii=False)


def write_to_xml(data, filename):
    root = etree.Element('root')
    numbers = etree.SubElement(root, 'number')
    numbers.append(etree.Comment(u"""数字信息"""))
    numbers.text = data

    xml = etree.ElementTree(root)
    xml.write(filename, pretty_print=True,
              xml_declaration=True, encoding='utf-8')


if __name__ == '__main__':
    try:
        data = read_from_excel('number.xls')
        write_to_xml(data, os.path.join(
            os.path.split(__file__)[0], 'number.xml'))
    except Exception as e:
        print(e)
