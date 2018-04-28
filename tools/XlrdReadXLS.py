# -*- coding: utf-8 -*- 
"""
@__author__ :70486 
@file: XlrdReadEXCEL.py
@time: 2017/12/10 16:13
@项目名称:operating
"""
import os

import xlrd


class EXCELXLRD:
    def __init__(self,_PATNNAME, sheet=0):
        # 判断文件是否存在
        if os.path.exists(_PATNNAME):
            self.excel = _PATNNAME
            self.data(sheet)
        else:
            raise FileNotFoundError('文件不存在！')

    def data(self, sheet):
        # 打开文件,读取文件的时候需要将formatting_info参数设置为True，默认是False
        # python3.x之后formatting_info默认为true
        self.workbook = xlrd.open_workbook(self.excel)

        if type(sheet) not in [int, str]:
            raise SheetTypeError('Please pass in <type int> or <type str>, not {0}'.format(type(sheet)))
        elif type(sheet) == int:
            # 根据索引获取sheet表
            self.sheetbook = self.workbook.sheet_by_index(sheet)
        else:
            try:
                # 根据索引获取sheet表
                self.sheetbook = self.workbook.sheet_by_name(sheet)
            except ValueError:
                from tools import DefinitionErrors
                raise DefinitionErrors('No sheet named <%r>' % sheet)

    # 返回该表总行数
    def rows_size(self):
        return self.sheetbook.nrows

    # 返回该表总列数
    def cols_size(self):
        return self.sheetbook.ncols

    # 返回指定行的内容
    def rowsValues(self,row = 0):
        return  self.sheetbook.col_values(row)

    # 返回指定列的内容
    def colValues(self,col = 0):
        return self.sheetbook.col_values(col)

    # 返回全部合并的内容
    # merged_cells返回的这四个参数的含义是：(row,row_range,col,col_range),
    # 其中[row,row_range)包括row,不包括row_range,col也是一样
    # 即(1, 3, 4, 5)的含义是：第1到2行（不包括3）合并，(7, 8, 2, 5)的含义是：第2到4列合并。
    def mergedCells(self):
        merge = self.sheetbook.merged_cells
        mergeList = []
        for index in merge:
            mergeList.append(sheet2.cell_value(index[0], index[2]))
        return mergeList

    # 返回合并单元格数量
    def merge_size(self):
        merge = self.sheetbook.merged_cells
        return merge

    def EXCEL_Content(self):
        nrows = self.rows_size()
        ncols = self.cols_size()
        rows_list = []
        cols_list = []
        print(nrows)
        print(ncols)
        # 遍历行
        for row in range(nrows):
            # 遍历列
            for col in range(ncols):
                if (self.sheetbook.cell(row, col).ctype == 3):  # 判断时间类型
                    date_value = xlrd.xldate_as_tuple(self.sheetbook.cell_value(row, col), workbook.datemode)
                    date_tmp = date(*date_value[:3]).strftime('%Y/%m/%d')
                    cols_list.append(date_tmp)
                elif (self.sheetbook.cell(row, col).ctype == 0):  # 判断空格类型
                    if len(self.sheetbook.merged_cells) > 0:
                        cols_list.append(self.sheetbook.cell(row, col).value)
                    else:
                        cols_list.append('null')
                elif (self.sheetbook.cell(row, col).ctype == 1):  # 判断字符串类型
                    cols_list.append(self.sheetbook.cell(row, col).value)
                else:# 其他类型的
                    cols_list.append(self.sheetbook.cell(row, col).value)
                    # cols_list.append(self.sheetbook.cell(row, col).value.encode('utf-8'))
        rows_list.append(cols_list)
        return rows_list


    def canshufangfa(self):
        # 获取所有sheet
        print(workbook.sheet_names())  # [u'sheet1', u'sheet2']

        # 根据sheet索引或者名称获取sheet内容
        print(workbook.sheet_by_index(0))
        print(workbook.sheet_by_name(workbook.sheet_names()[0]))
        print(workbook.sheet_by_name(u'name'))

        print("leixing %s" % self.sheet.cell(row, col).ctype) # 打印指定单元格的数据类型

        # 获取单元格内容
        print(self.sheet.cell(1, 0).value.encode('utf-8'))
        print( self.sheet.cell_value(1, 0).encode('utf-8'))
        print(self.sheet.row(1)[0].value.encode('utf-8'))

if __name__ == '__main__':
    report_path = os.path.join(os.getcwd(),'nihao.xls')
    print(report_path)
    ex = EXCELXLRD(report_path)
    print(ex.EXCEL_Content())
    values = ex.rowsValues(0)
    for va in values:
        print(va)
