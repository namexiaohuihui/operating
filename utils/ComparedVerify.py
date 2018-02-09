# -*- coding: utf-8 -*-
__author__ = 'DingDong'
"""
@file: ComparedVerify.py
@time: 2018/2/5 10:30
"""
import inspect
import os
import time

from utils.operation.selenium_input import action_input
from utils.RewriteThread import inherit_thread as th
from utils.browser_establish import browser_confirm
from utils.config import readModel
from utils.operation.selenium_click import action_click
from utils.PymysqlMain import pymysqls
from utils import DefinitionErrors as dError
from utils.OpenpyxlExcel import READEXCEL, PANDASDATA


class compared_verify(object):
    vac = action_click()
    vai = action_input()

    """
        单例类的用法：
        用于连接两个类之间的数据数据。
        通过第三方来传递信息
    """

    def __new__(cls, *args, **kw):
        # 单例类判断。如果该类创建过就不需要重新创建了
        if not hasattr(cls, '_instance'):
            orig = super(compared_verify, cls)
            cls._instance = orig.__new__(cls, *args, **kw)
        return cls._instance

    # 在字符串str查找ing出现的位置.从number下标开始找,返回-1表示找不到
    def string_lookup_find(self, str, ing, number=0):
        nPos = str.find(ing, number)
        if nPos != -1:
            return True
        else:
            return False

    """
       # ------------------内容参数的比较------------------------
   """

    def _verify_parameter(self, content):
        if content is None:
            content = ''
        return content

    """
    #------------------获取浏览器部分------------------------------------
    """

    def _browser(self, option):
        # 1.创建浏览器所在函数的对象
        bc = browser_confirm.__new__(browser_confirm)

        conf = readModel.establish_con(model="model")
        url = conf.get("wap", option)

        # 2.调用已经规划好的浏览器函数
        self.driver = bc.url_opens(url)
        return self.driver

    """
       #--------------------读取excel表格数据部分-----------------------------------------
   """

    def _read_excel(self, filename, SHEETNAME=1):
        """
            从excel表格中获取数据并进行转换
            :param file_path:
            :return:
            """
        # 获取excel路径
        file_path = readModel.establish_con(model="excelmodel").get("excel", filename)

        # 读取相应路径中的数据
        read = READEXCEL(file_path, SHEETNAME=SHEETNAME)

        return read

    def _conversion_pandas(self, row_col_data, title_data=None, columnLabel=None):
        # 数据转换
        pan = PANDASDATA(row_col_data)

        df = pan.dataFrame(columns=title_data)  # 设置标题名

        if columnLabel != None:
            df = df.set_index([columnLabel])  # 设置df数据中的序列号

        return df

    def _excel_Data(self, filename, SHEETNAME=1):
        # 获取excel对象
        read = self._read_excel(filename, SHEETNAME)

        # 获取case
        whole = read.position_sheet_row_value()

        # 将case中内容的数据读出
        row_col_data = whole[0]

        # 将case中标题的内容读出
        title_data = whole[1]

        # 获取case中某个指定key的内容读出
        columnLabel = read.die_angegebene_keys(row_col_data=row_col_data, title_data=title_data)

        excelData = self._conversion_pandas(row_col_data, title_data, columnLabel)  # 设置df数据中的序列号

        return excelData

    """
        #--------------------元素判断部分-----------------------------------------
    """

    def _visible_return_selectop(self, locator, timeout=5):
        # 判断元素是否存在，如果存在就进行点击并返回对象
        ele = self.vac.is_visible_css_selectop(self.driver, locator)
        return ele

    def _visible_css_selectop(self, locator, timeout=5):
        # 判断元素是否存在，如果存在就进行点击并返回对象
        self.vac.css_click(self.driver, locator)

    def _visible_css_selectop_text(self, locator):
        # 判断元素是否存在，如果存在就进行获取元素的text属性
        _text = self.vai._visible_selectop_text(self.driver, locator)
        return _text

    def _visible_css_selectop_attribute(self, locator):
        # 判断元素是否存在，如果存在就获取元素的value属性内容
        self.vai._visible_selectop_attribute(self.driver, locator)

    def _sendKeys_css_selectop(self, locator, content):
        # 判断元素是否存在，如果存在就进行输入
        self.vai.css_input(self.driver, locator, content)

    def _visible_json_click(self, locator):
        self.vac.id_confirm_prompt(self.driver, locator)

    def _visible_json_input(self, ordinal, parameter):
        self.vai.id_js_input(self.driver, ordinal, parameter)

    """
    # 数据库查询及内容返回
    """

    def create_database(self):
        pm = pymysqls()

        pm.connects_readModel()

        return pm

    def mysql_single_selects(self, sql):
        pm = self.create_database()
        result = pm.single_selects(sql)
        pm.closes()

        return result

    def mysql_total_selects(self, sql):
        pm = self.create_database()
        result = pm.total_vertical_selects(sql)
        pm.closes()

        return result

    """
    #--------------------其他一些配置部分-----------------------------------------
    """

    def sleep_time(self, times=1):
        time.sleep(times)

    def error_log(self, function):
        # 执行文件的文件名
        basename = os.path.splitext(os.path.basename(__file__))[0]

        # 拼接名字
        name_tion = basename + "_" + function

        # 调用错误类
        dError.error_output(name_tion, self.driver)

    def _start_thread_pool(self, funktion):  # 开启线程池
        # funktion = [ap._excel_Data, get_basename]  # 该列表存放需要执行的函数
        print("Opening thread execution %s" % time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
        faden = []  # 该列表存放已经开启的线程

        inhalt = []  # 该列表存放线程中所执行的函数返回值内容

        for para in funktion:  # 遍历函数开启线程
            threads = th(para)
            faden.append(threads)
            threads.start()

        for argu in faden:  # 开启的线程中，进行阻塞，当子线程完成之后才继续下一步
            argu.join()
            inhalt.append(argu.get_result())

        # overall_ExcelData = inhalt[0]  # df转换的数据，方便对excel进行操作r
        print("Thread execution finished %s" % time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
        return inhalt
