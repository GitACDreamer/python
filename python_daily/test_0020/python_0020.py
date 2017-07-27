# coding=utf-8
# @author: Leland
# @email:  AC_Dreamer@163.com
# @date:   2017-07-23 13:45:26
# @title:  通话详单.xls 文件，对每月通话时间做个统计。

import xlrd

def statistics_phone_record(filename):
    xls = xlrd.open_workbook(filename)
    sheet = xls.sheet_by_index(0)
    times = 0
    for i in range(1 ,sheet.nrows):
        times += int(sheet.cell_value(i , 3))
    print('月通话时长：%d小时%d分%d秒' %(times/3600 , (times%3600)/60 , times%3600%60))
    

if __name__ == '__main__':
    try:
        statistics_phone_record('src.xls')
    except Exception as e:
        print(e)