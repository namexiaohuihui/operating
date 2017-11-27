# -*- coding: utf-8 -*-
__author__ = 'Administrator'
"""
http://blog.csdn.net/chengxuyuanyonghu/article/details/54951399
数据类型
    ctype : 0 empty,1 string, 2 number, 3 date, 4 boolean, 5 error  
@file: readExle.py
@time: 2017/11/17 0:07
"""
import xlrd
from datetime import date, datetime


def read_excel():
    # 打开文件,读取文件的时候需要将formatting_info参数设置为True，默认是False
    # 3.x之后默认为true
    workbook = xlrd.open_workbook(r'E:\demo.xlsx')
    # 获取所有sheet
    print(workbook.sheet_names())  # [u'sheet1', u'sheet2']

    sheet2_name = workbook.sheet_names()[1]

    # 根据sheet索引或者名称获取sheet内容
    sheet2 = workbook.sheet_by_index(1)  # sheet索引从0开始
    sheet2 = workbook.sheet_by_name('Sheet4')

    # sheet的名称，行数，列数
    print(sheet2.name, sheet2.nrows, sheet2.ncols)

    # 获取整行和整列的值（数组）
    rows = sheet2.row_values(3)  # 获取第四行内容
    cols = sheet2.col_values(2)  # 获取第三列内容
    print(rows)
    print(cols)
    for row in range(sheet2.nrows):
        for col in range(sheet2.ncols):
            #print("leixing %s" % sheet2.cell(row, col).ctype)
            if (sheet2.cell(row, col).ctype == 3):
                date_value = xlrd.xldate_as_tuple(sheet2.cell_value(row, col), workbook.datemode)
                date_tmp = date(*date_value[:3]).strftime('%Y/%m/%d')
                print("hsijian %s" % date_tmp)
            if (sheet2.cell(row, col).ctype == 0):
                merge = sheet2.merged_cells
                for index in merge:
                    print(index[0],index[2],row,col)
                    if index[0] == row & index[2]-1==col:
                        print("kongge %s" % sheet2.cell_value(index[0], index[2]))
                #print("kongge %s" % sheet2.row_values(row)[col])
            #print("waim %s" % sheet2.cell(row, col).value)
        print("------------------------")

    # 获取单元格内容
    # print(sheet2.cell(1, 0).value.encode('utf-8'))
    # print( sheet2.cell_value(1, 0).encode('utf-8'))
    # print(sheet2.row(1)[0].value.encode('utf-8'))

    print(sheet2.row_values(7)[2])  # 读取合并单元格的内容

    # 返回页面上所以合并格的位置
    # merged_cells返回的这四个参数的含义是：(row,row_range,col,col_range),
    # 其中[row,row_range)包括row,不包括row_range,
    # col也是一样，
    # 即(1, 3, 4, 5)的含义是：第1到2行（不包括3）合并，(7, 8, 2, 5)的含义是：第2到4列合并。

    print(sheet2.merged_cells)
    merge = sheet2.merged_cells

    for index in merge:
        print(sheet2.cell_value(index[0], index[2]))


def rowcol():
    if (sheet.cell(row, col).ctype == 3):
        date_value = xlrd.xldate_as_tuple(sheet.cell_value(rows, 3), book.datemode)
        date_tmp = date(*date_value[:3]).strftime('%Y/%m/%d')

        # 将时间数据拆分 （年，月，日，时，分，秒）
        date_value = xlrd.xldate_as_tuple(sheet2.cell_value(2, 2), workbook.datemode)
        # 获取时间格式的前三个:datetime.date(年，月，日)
        date_mess = date(*date_value[:3])
        # 转换格式
        str = date_mess.strftime('%Y/%m/%d')
        print(str)


if __name__ == '__main__':
    read_excel()
