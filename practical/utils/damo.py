# -*- coding: utf-8 -*-
__author__ = 'Administrator'
"""
@file: damo.py
@time: 2017/11/17 1:21

http://blog.csdn.net/Tulaimes/article/details/71172778
"""

import xlwt


def set_style(name, height,color, bold=False):
    style = xlwt.XFStyle()  # 初始化样式

    font = xlwt.Font()  # 为样式创建字体
    # 字体类型：比如宋体、仿宋
    font.name = name
    # 是否为粗体
    font.bold = bold
    # 设置字体颜色
    font.colour_index = color
    # 字体大小
    font.height = height
    # 字体是否斜体
    font.italic = True
    # 字体下划,当值为11时。填充颜色就是蓝色
    font.underline = color
    # 字体中是否有横线struck_out
    font.struck_out =True


    # 定义格式
    style.font = font

    return style

# 创建工作簿,并指定写入的格式
f = xlwt.Workbook(encoding='utf8')  # 创建工作簿

#  创建sheet，并指定可以重复写入数据的情况.设置行高度
sheet1 = f.add_sheet(u'sheet1', cell_overwrite_ok=False)
row0 = [u'业务', u'状态', u'北京', u'上海', u'广州', u'深圳', u'状态小计', u'合计','绩效','范围']
# 生成第一行
for i in range(0, 10):
    # 参数对应：行，列，值，字体样式(可以没有)
    if i%2==0:
        sheet1.write(i, 0, row0[i%10], set_style('Times New Roman', 220,i, True))
    else:
        sheet1.write(i, 0, row0[i%10],  set_style('汉仪瘦金书繁', 220,i, False))

f.save('demopy.xls')  # 保存文档