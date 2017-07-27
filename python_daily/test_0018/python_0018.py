# coding=utf-8
# @author:Leland
# @email: AC_Dreamer@163.com
# @date:  2017-07-23 11:20:46
# @title: 将excel文件读写到xml里面

import os
import xlrd
import json
from lxml import etree

def read_from_excel(filename):
    xls = xlrd.open_workbook(filename)
    sheet = xls.sheet_by_name('city')
    data = {}
    for i in range(sheet.nrows):
        data[sheet.row_values(i)[0]] = sheet.row_values(i)[1]
    return json.dumps(data , ensure_ascii=False) # ensure_ascii = False可以解决中文字符被编码成Unicode


def write_to_xml(data, filename):
    root = etree.Element("root")
    citys = etree.SubElement(root , 'city')
    citys.append(etree.Comment(u"""城市信息"""))
    citys.text = data

    city_xml = etree.ElementTree(root)
    city_xml.write(filename, pretty_print=True, xml_declaration=True, encoding='utf-8')

if __name__ == '__main__':
    try:
        data = read_from_excel('city.xls')
        write_to_xml(data, os.path.join(os.path.split(__file__)[0], 'city.xml'))
    except Exception as e:
        print(e)
