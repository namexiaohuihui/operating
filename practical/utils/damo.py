# -*- coding: utf-8 -*-
__author__ = 'Administrator'
"""
@file: damo.py
@time: 2017/11/17 1:21
"""

import xlwt


def set_style(name, height, bold=False):
    style = xlwt.XFStyle()  # 初始化样式

    font = xlwt.Font()  # 为样式创建字体
    font.name = name  # 'Times New Roman'
    font.bold = bold
    font.color_index = 4
    font.height = height

    # borders= xlwt.Borders()
    # borders.left= 6
    # borders.right= 6
    # borders.top= 6
    # borders.bottom= 6

    style.font = font
    # style.borders = borders

    return style

f = xlwt.Workbook()  # 创建工作簿
sheet1 = f.add_sheet(u'sheet1', cell_overwrite_ok=False)  # 创建sheet
row0 = [u'业务', u'状态', u'北京', u'上海', u'广州', u'深圳', u'状态小计', u'合计']
# 生成第一行
for i in range(0, len(row0)):
    sheet1.write(0, i, row0[i], set_style('Times New Roman', 220, True))
f.save('demo5.xls')  # 保存文