# -*- coding: utf-8 -*- 
"""
@__author__ :70486 
@file: OpenpyxlExcel.py
@time: 2017/12/9 18:39
@项目名称:operating
http://openpyxl.readthedocs.io/en/latest/
http://openpyxl.readthedocs.io/en/default/usage.html#write-a-workbook
"""
from openpyxl import Workbook
from openpyxl import load_workbook
from openpyxl.compat import  range
from openpyxl.utils import get_column_letter
import datetime
def read():
    # 创建工作表
    wb = Workbook()
    # 定义文件名
    dest_filename = 'empty_book.xlsx'
    # 打开工作薄，默认第一个
    ws1 = wb.active
    # 设置工作薄的名称
    ws1.title = 'range names'

    for row in range(1, 40):
        ws1.append(range(600))
    ws1['A43'] = '傻逼'
    # 设置指定位置的工作薄的名称
    ws2 = wb.create_sheet(title='Pi',index = 3)
    # 复制给单元格
    ws2['F5'] = 3.14
    # 设置工作破名称，在现有工作薄的后面增加
    ws3 = wb.create_sheet(title='Data')
    for row in range(10, 20):
        for col in range(27, 54):
            # 指定位置并写入内容
            _ = ws3.cell(column=col, row=row, value="{0}".format(get_column_letter(col)))

    print(ws3['AA10'].value)

    wb.save(filename=dest_filename)

def load():
    # 要操作的表格
    wb = load_workbook(filename='empty_book2.xlsx')
    # 获取指定工作簿
    ws = wb['range names']
    # 打印指定的内容:ws['A4']返回的是一个cell，通过value来获取值
    # print(ws['A4'].value)
    # print(ws['A4'])
    '''
    打印工作薄名称
    print(wb.sheetnames)
    for sheet in wb :
        print(sheet.title)
    '''
    # 复制工作薄，并且不会新建一个工作薄，只是暂时的
    # 如果本体是只读或者只写的情况就不能复制
    #　wb.copy_worksheet(sheet_ranges)

    # 返回指定的行列对象。。注意有双层的lit
    '''
    cell_range = sheet_ranges['A1':'C2']
    print(cell_range)
    for va in cell_range:
        print(va)
        for v in va:
            print(v.value)
    '''

    # 获取整行或者整列的内容
    '''
    colC = ws['C']
    col_range = ws['C:D']
    row10 = ws[10]
    row_range = ws['5:10']
    
    for row in ws.iter_rows(min_row=1,max_row=2,max_col=3):
        print(row)
        
    for row in ws.iter_cols(min_row=1,max_row=2,max_col=3):
        print(row)
    
    # 打印所有的行和列
    print(tuple(ws.rows)) #单行中，列的长度
    print(tuple(ws.columns))　＃单列中，行的长度
    '''
    '''
    # 将现有的表进行复制并保存为模板。。并后缀名为xltx，如果为xls和xlsx在打开的时候出现问题
    wb = load_workbook('document.xlsx')
    wb.template = True
    wb.save('document_template.xltx')
    wb.save('document_template2.xls')
    
    
    # 将现有的模板还原成文档或直接将现有的wb另存为。
    # 保存为xls文件打开的时候会提示错误
    wb = load_workbook('document_template.xltx')
    wb.template = False
    wb.save('nihaoma.xlsx')
    wb.save('nihaoma.xls')
    '''
    print(wb.sheetnames)
    print(wb.get_sheet_names)






def date():
    wb = Workbook()

    dest_filename = 'empty_book2.xlsx'

    ws = wb.active
    ws.title = 'range names'

    dt = datetime.datetime.now()
    # 时间转时间戳print(dt.timestamp())
    # 时间戳转时间print(dt.fromtimestamp())
    ws['A1'] = dt #　写入时间
    print(ws['A1'].number_format)

    # You can enable type inference on a case-by-case basis
    #　还可以启用类型和格式推断：
    wb.guess_types = True
    ws['B1'] = '3.14%'
    print(ws['B1'].value)
    print(ws['B1'].number_format)
    # set percentage using a string followed by the percent sign
    wb.guess_types = True
    print(ws['B1'].value)
    print(ws['B1'].number_format)

    #　写入求和内容
    ws['C1'] = "=SUM(1,1)"
    print(ws['C1'].value)
    print(ws['C1'].number_format)

    # 判断是否使用公式
    from openpyxl.utils import  FORMULAE
    kk = "HEX2DEC" in FORMULAE
    print(kk)

    # 单元格合并以及删除
    for row in range(2, 6):
        ws.append(range(5))
    ws.merge_cells('A2:D2')
    ws.unmerge_cells('A2:D2')
    # 等价于上面的
    ws.merge_cells(start_row=4, start_column=1, end_row=4, end_column=4)
    ws.unmerge_cells(start_row=4, start_column=1, end_row=4, end_column=4)
    """
    # 保存图片,影响运行屏蔽先
    from openpyxl.drawing.image import Image
    ws['A6'] = "You should see three logos below"
    img = Image("F:\\图片\\22.jpg")
    ws.add_image(img,'A6')
    """
    #折叠柱（轮廓）（将指定的列进行折叠）
    # ws.column_dimensions.group('A', 'A', hidden=True)
    # 设置工作薄标题颜色
    ws.sheet_properties.tabColor = '1072BA'
    # 保存文件，但不警告会覆盖文件
    wb.save(dest_filename)

if __name__ == '__main__':
    #　date()
    load()