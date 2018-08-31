# -*- coding: utf-8 -*- 
"""
@__author__ :70486 
@file: XlwtWriteEXCEL.py
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

    def __init__(self, name='sheet1'):
        # 创建工作簿,并指定写入的格式
        self.workbook = xlwt.Workbook(encoding='utf8')  # 创建工作簿

        #  创建sheet，并指定可以重复写入数据的情况.设置行高度
        self.sheet = self.workbook.add_sheet(name, cell_overwrite_ok=False)

        # 初始化样式
        self.style = xlwt.XFStyle()

    def FontStyle(self, name='Times New Roman', height=220, color=32, bold=False):
        '''
        font._weight = 0x02BC   :值为0x02BC时显示为粗体，其余值时不详
        好像是设置偏移量:再有下划线做比较时，字体的下部分在下划线的上面
        font.escapement = 300
        以下是目前未知的属性
        font.charset = color、font.outline = True、font.shadow = True

        属性 ： 关系
        bold:粗体（是否）/italic:斜体（是否）/struck_out:字体中横线(是否)
        underline:下划线（大小）
        :param name:
        :param height:
        :param color:
        :param bold:
        :return:
        '''
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

    def bordersFrame(self, color):
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

    def Size_Width(self, width=3333):
        # 设置列的宽度
        self.sheet.col(0).width = width

    # 　目前不行
    def Hyperlink(self, url="http://www.baidu.com", name="baidu"):
        # 添加超链接。。
        mula = xlwt.Formula('HYPERLINK("http://www.baidu.com";+"+name+"+)')
        # 　sheet1.write(0, 2, mula)

    """
    设置格式背景颜色
    """

    def backgroundPattern(self, color=2):
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
        # 　sheet1.write(0, 3, 'Cell Contents', style1)

    def qitahanghaufjk(self):
        # 写入内容的方式
        sheet1.write(0, i, row0[i])  # 行列，内容
        # 行，列，内容，写入的类型
        sheet1.write(0, i, row0[i], self.set_style('Times New Roman', 220, True))
        #   write_merge(x, x + m, y, w + n, string, sytle)
        #   x表示行，y表示列，m表示跨行个数，n表示跨列个数，string表示要写入的单元格内容，style表示单元格样式。
        #   其中，x，y，w，h，都是以0开始计算的。
        #   写合并单元格的方式,从21行到21中的，第0列到第1列单元格进行合并
        #   行数相等说明，行的单元格不用合并，列数相等，说明列的单元格不用进行合并
        sheet1.write_merge(21, 21, 0, 1, u'合计', self.set_style('Times New Roman', 220, True))


class demoTest:
    def set_style(self, name, height, bold=False):
        style = xlwt.XFStyle()  # 初始化样式

        font = xlwt.Font()  # 为样式创建字体
        font.name = name  # 'Times New Roman'
        font.bold = bold
        font.color_index = 4
        font.height = height

        style.font = font

        return style

    # 写excel
    def write_excel(self):
        f = xlwt.Workbook()  # 创建工作簿

        ''''' 
        创建第一个sheet: 
          sheet1 
        '''
        sheet1 = f.add_sheet(u'sheet1', cell_overwrite_ok=False)  # 创建sheet
        row0 = [u'业务', u'状态', u'北京', u'上海', u'广州', u'深圳', u'状态小计', u'合计']
        column0 = [u'机票', u'船票', u'火车票', u'汽车票', u'其它']
        status = [u'预订', u'出票', u'退票', u'业务小计']

        # 生成第一行
        for i in range(0, len(row0)):
            sheet1.write(0, i, row0[i], self.set_style('Times New Roman', 220, True))

        # 生成第一列和最后一列(合并4行)
        i, j = 1, 0
        while i < 4 * len(column0) and j < len(column0):
            '''
            write_merge(x, x + m, y, w + n, string, sytle)
            x表示行，y表示列，m表示跨行个数，n表示跨列个数，string表示要写入的单元格内容，style表示单元格样式。
            其中，x，y，w，h，都是以0开始计算的。

            如上述：sheet1.write_merge(21,21,0,1,u'合计', self.set_style('Times New Roman',220,True))

            即在22行合并第1,2列，合并后的单元格内容为"合计"，并设置了style。
            '''
            sheet1.write_merge(i, i + 3, 0, 0, column0[j], self.set_style('Arial', 220, True))  # 第一列
            sheet1.write_merge(i, i + 3, 7, 7)  # 最后一列"合计"
            i += 4
            j += 1

        sheet1.write_merge(21, 21, 0, 1, u'合计', self.set_style('Times New Roman', 220, True))
        sheet1.write_merge(22, 22, 0, 5, u'测试', self.set_style('Times New Roman', 220, True))

        # 生成第二列
        i = 0
        while i < 4 * len(column0):
            for j in range(0, len(status)):
                sheet1.write(j + i + 1, 1, status[j])
            i += 4

        f.save('222.xls')  # 保存文件


if __name__ == '__main__':
    demoTest.write_excel(demoTest())
    # generate_workbook()
    # read_excel()
    # ex = EXCELXLWT(name = 'name')
    # ex.FontStyle()
    # for i in range(5):
    #     ex.sheet.write(i, 5, i, ex.style)
    # ex.workbook.save('nihao.xls')
