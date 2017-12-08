# -*- coding: utf-8 -*- 
"""
@__author__ :70486 
@file: WriteEXCEL.py
@time: 2017/12/6 22:45
@项目名称:operating
"""
import xlwt

class EXCELXLWT:

    """
    font字体
    alignment对齐
    borders边界
    pattern模式(设置背景)
    protection保护(没用过)
    """
    def __init__(self,name = 'sheet1'):
        # 创建工作簿,并指定写入的格式
        self.workbook = xlwt.Workbook(encoding='utf8')  # 创建工作簿

        #  创建sheet，并指定可以重复写入数据的情况.设置行高度
        self.sheet = f.add_sheet(name, cell_overwrite_ok=False)

        # 初始化样式
        self.style = xlwt.XFStyle()


    """
    font._weight = 0x02BC   :值为0x02BC时显示为粗体，其余值时不详
    好像是设置偏移量:再有下划线做比较时，字体的下部分在下划线的上面
    font.escapement = 300
    以下是目前未知的属性
    font.charset = color、font.outline = True、font.shadow = True
        
    属性 ： 关系
    bold:粗体（是否）/italic:斜体（是否）/struck_out:字体中横线(是否)
    underline:下划线（大小）
    """
    def FontStyle(self,name, height,color, bold=False):
        font = xlwt.Font()  # 为样式创建字体
        # 字体类型：比如宋体、仿宋
        font.name = name
        # 设置字体颜色
        font.colour_index = color
        # 字体大小
        font.height = height
        # 定义格式
        self.style.font = font

    """
    # borders.left = xlwt.Borders.DASHED
    # DASHED虚线
    # NO_LINE没有
    # THIN实线
    """
    def bordersFrame(self):
        # 设置边框：上下左右的样式
        borders = xlwt.Borders()
        borders.left = color
        borders.right = color
        borders.top = color
        borders.bottom = color

        self.style.borders = borders

    """
    color
    """
    def timeStyle(self):
        import time
        now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
        # self.sheet.write(0, 1, now, self.style)

    """
    设置宽度
    """
    def Size_Width(self,width = 3333):
        # 设置列的宽度
        self.sheet.col(0).width = width

    #　目前不行
    def Hyperlink(self,url = "http://www.baidu.com" ,name = "baidu"):
        # 添加超链接。。
        mula = xlwt.Formula('HYPERLINK("http://www.baidu.com";+"+name+"+)')
        #　sheet1.write(0, 2, mula)

    """
    设置格式背景颜色
    """
    def backgroundPattern(self,color = 2):
        # 设置背景颜色
        pattern = xlwt.Pattern()
        # 设置背景颜色的模式
        pattern.pattern = xlwt.Pattern.SOLID_PATTERN

        # 各数值之间代表的颜色: 0 =黑色，1 =白色，2 =红色，
        # 3 = 4 =绿色，蓝色，5黄色，6 =品红，
        # 7 =青色，16 = 17 =栗色，深绿色，18 =深蓝色，
        # 19 =暗黄色，棕色），几乎20 =暗红色，21 =水鸭（Teal），
        # 22 = 23 =浅灰色，深灰色，后续自己找…
        # 背景颜色
        pattern.pattern_fore_colour = color

        self.style.pattern = pattern
        #　sheet1.write(0, 3, 'Cell Contents', style1)
