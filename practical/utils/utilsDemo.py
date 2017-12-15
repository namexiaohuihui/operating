# -*- coding: utf-8 -*-
__author__ = 'Administrator'
"""
@file: utilsDemo.py
@time: 2017/12/13 15:18
"""
from openpyxl import Workbook
from openpyxl import load_workbook
from openpyxl.compat import range
from openpyxl.utils import get_column_letter


def read():
    # 创建工作表
    wb = Workbook()
    # 定义文件名
    dest_filename = 'empty_book.xlsx'
    ws = wb.active
    ws.title = 'range names'

    # 将现有的数据进行表格显示
    from openpyxl.chart import BarChart, Reference, Series
    for i in range(2,12):
        ws.append(range(1,5))
    # 制作表格的数据范围
    values = Reference(ws, min_col=1, min_row=1, max_col=6, max_row=4)
    chart = BarChart()  # 指定表格对象
    # from_rows控制以行为单位显示还是以列为单位显示，titles_from_data控制标题
    chart.add_data(values, from_rows = True)
    ws.add_chart(chart, 'E12')

    wb.save(filename=dest_filename)

def date():
    wb = Workbook()

    dest_filename = 'SampleChart.xlsx'

    ws = wb.active
    ws.title = 'range names'



    '''
    # 将现有的数据进行表格显示
    from openpyxl.chart import BarChart, Reference, Series
    for i in range(10):
        ws.append([1])
    # 制作表格的数据范围
    values = Reference(ws, min_col=1, min_row=1, max_col=1, max_row=10)
    chart = BarChart()# 指定表格对象
    # from_rows控制每个树状图的颜色，titles_from_data控制标题
    chart.add_data(values,from_rows=True,titles_from_data=True)
    ws.add_chart(chart, 'E12')
    '''

    '''
    # 添加标红注释
    from openpyxl.comments import Comment
    comment = Comment('This is the comment text', 'Comment Author')
    print(comment.text)
    print(comment.author)
    ws['A1'].comment = comment
    '''
    # 折叠柱（轮廓）（将指定的列进行折叠）
    # ws.column_dimensions.group('A', 'A', hidden=True)
    # 设置工作薄标题颜色
    ws.sheet_properties.tabColor = '1072BA'

    # 保存文件，但不警告会覆盖文件
    wb.save(dest_filename)


def pandsaaa():
    import pandas as pd
    # 将list的内容通过整形进行索引
    nk = {'key': {'foo1', 'foo2'}, 'lval': {'value'}}
    # left = pd.Series(['1', '2', '3', nk, '7'])
    left = pd.Series(nk)
    print(left)

    # 定义索引之后对数据进行排列
    # 1. 定义索引
    dates = pd.date_range('20171201', periods=6)
    # 转换
    df = pd.DataFrame(pd.Timedelta('20130102'), dates, list('ABCD'))
    print(df)

    from openpyxl.utils import dataframe
    from openpyxl.utils.dataframe import dataframe_to_rows
    import pandas as pd
    import numpy
    # 对数据进行有效的排列,将不同数据中key相同的数据进行组合
    inp = [{'c1': 10, 'c2': 100}, {'c1': 11, 'c2': 110}, {'c1': 12, 'c2': 120},
           {'c1': 10}]
    df = pd.DataFrame(inp)
    print(df)
    print(df.iloc[2])  # 打印数据的同时也打印了数据类型以及ｎａｍｅ
    for x in range(len(df.index)):
        print(df['c1'].iloc[x].dtype)  # 指定列的内容，并打印数据类型v

        # pandas和numpy 可以直接对列表数据进行排序以及读取。。
        # 可以对ｊｓｏｎ返回的数据库信息进行解析

    inp = [{'c1': 10, 'c2': 100}, {'c1': 11, 'c2': 110}, {'c1': 12, 'c2': 120}]
    df = pd.DataFrame(inp)
    for r in dataframe_to_rows(df, index=True, header=True):
        print(r)

    print("*************")
    df = pd.DataFrame({'a': [1, 2, 3], 'b': ['a', 'b', 'c'], 'c': ["A", "B", "C"]})
    for i, row in enumerate(df.values):
        index = df.index[i]
        print(row)




if __name__ == '__main__':
    read()
    # 　load()


