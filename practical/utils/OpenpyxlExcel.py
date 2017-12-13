# -*- coding: utf-8 -*- 
"""
@__author__ :70486 
@file: OpenpyxlExcel.py
@time: 2017/12/9 18:39
@项目名称:operating
http://openpyxl.readthedocs.io/en/latest/
http://openpyxl.readthedocs.io/en/default/usage.html#write-a-workbook
http://blog.csdn.net/tanzuozhev/article/details/76713387
http://www.cnblogs.com/chaosimple/p/4153083.html
"""

from openpyxl import Workbook
from openpyxl import load_workbook
from openpyxl.compat import range
from openpyxl.utils import get_column_letter
import datetime
import os

"""
这个class负责读取数据：从excel中读取数据到电脑
"""


class READEXCEL:
    def __init__(self, FILEPATH, SHEETNAME=None):
        # 判断文件是否存在
        if os.path.exists(FILEPATH):
            self.excel = FILEPATH

            # 判断是否为空
            if SHEETNAME == None:
                self.data(0)
            else:
                self.data(SHEETNAME)
        else:
            raise FileNotFoundError('文件不存在！')

    def data(self, sheet):

        # 创建需要操作的文档
        self.workbook = load_workbook(filename=self.excel)  # 打开文档

        # 判断是根据数字还是文字进行读取sheet，如果是数字的话必须小于现有的长度
        if type(sheet) in [int] and sheet < len(self.workbook.sheetnames):
            self.sheetbook = self.workbook[self.workbook.sheetnames[sheet]]

        # 如果是文字
        elif type(sheet) in [str]:
            self.sheetbook = self.workbook[self.workbook.sheetnames[0]]

        # 长度过长时提示
        elif sheet >= len(self.workbook.sheetnames):
            print("sheet索要的位置大于现有的长度")

        # 最后输出
        else:
            print("你输入啥咯.")

    #   返回需要读取cell的内容
    def get_sheet_value(self, range):
        # 先判断需要寻找的cell位置。如果为空或者其他类型的就提示
        if type(range) in [int, str]:
            content = self.sheetbook[range]
            return content
        else:
            print('1级错误')

    #   工作薄的名称
    def get_sheet_title(self):
        return self.sheetbook.title

    #   返回某个列的标题位置名称
    def get_column_letter(self,Number = 1):
        return get_column_letter(Number)


"""
这个class负责写入数据：将信息从电脑写到excel
"""


class WRITEEXCEL:
    def __init__(self):
        print()


if __name__ == '__main__':
    read_excel = READEXCEL('empty_book.xlsx')
    # print(read_excel.get_sheet_value('1'))
    print(read_excel.get_column_letter(1))
    for kk in read_excel.get_sheet_value(1):
        print(kk.value)
