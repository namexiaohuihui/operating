# -*- coding: utf-8 -*-
__author__ = 'DingDong'
"""
@file: ComparedVerify.py
@time: 2018/2/5 10:30
"""
import json
import operator  # 任何对象都可以比较功能
import os
import sys
import time

from tools import DefinitionErrors as dError
from tools.PymysqlMain import pymysqls
from utils.browser_establish import browser_confirm
from utils.config import readModel
from utils.operation.selenium_click import action_click
from utils.operation.selenium_input import action_input


class ComparedVerify(object):
    vac = action_click()
    vai = action_input()

    def __new__(cls, *args, **kw):
        """
        单例类判断。如果该类创建过就不需要重新创建了
        单例类的用法：
        用于连接两个类之间的数据数据。
        通过第三方来传递信息
        :param args:
        :param kw:
        :return:
        """
        if not hasattr(cls, '_instance'):
            orig = super(ComparedVerify, cls)
            cls._instance = orig.__new__(cls)
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

    def operator_dataframe(self, reValue: object, excleValue: object):
        self.log.info("读取:  %s  类型 :  %s " % (reValue, type(reValue)))
        self.log.info("获得:  %s  类型 :  %s " % (excleValue, type(excleValue)))

    def _verify_operator(self, reValue: object, excleValue: object) -> "通过assert断言形式进行比较":
        """
        简单的数据比较：list、dict、str、int、bool等数据类型
        :param reValue:  数据源
        :param excleValue:  比较源
        :return:
        """
        self.operator_dataframe(reValue, excleValue)
        assert reValue == excleValue, "_verify_operator 数据比较错误，用例不通过处理。"

    def _verify_operator_dataframe(self, reValue: "pandas类型的数据源", excleValue: "pandas类型的比较源") -> ("dataFrame数据类型进行比较"):
        self.operator_dataframe(reValue, excleValue)
        return operator.eq(reValue, excleValue)

    def _verify_parameter(self, content):
        if content is None:
            content = ''
        return content

    def stringToValueBoolean(self, value):
        _value = operator.eq(value, "true")
        return _value

    def number_cutting(self, attribute: "某个需要切割的数据") -> "对字符串中的数据进行id切割":
        print("{}------->公告的id数据 ".format(attribute))
        ribute = str.split(attribute, "/", 4)
        if "/" in ribute[4]:
            return str.split(ribute[4], "/")[0]
        else:
            return ribute[4]

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

    # def conversionPandas(self, row_col_data, title_data=None, columnLabel=None):
    #     # # 数据转换
    #     # pan = PANDASDATA(row_col_data)
    #     #
    #     # df = pan.dataFrame(columns=title_data)  # 设置标题名
    #     #
    #     # if columnLabel != None:
    #     #     df = df.set_index([columnLabel])  # 设置df数据中的序列号
    #
    #     read = OpenExcelPandas(row_col_data, title_data)
    #     df = read.conversionPandas()
    #     return df

    """
        #--------------------元素判断部分-----------------------------------------
    """

    def _visible_returan_tag_name(self, ele, locator, timeout=5):
        loca_ele = self.vac.ele_visible_tag_name(ele, locator, timeout)
        return loca_ele

    def _visible_returns_selectop(self, locator, timeout=5):
        # 根据元素组path来查找元素，并将元素组进行返回
        ele = self.vac.is_visibles_css_selectop(self.driver, locator)
        return ele

    def _visible_return_selectop(self, locator, timeout=5):
        # 判断元素是否存在，如果存在就返回该元素
        ele = self.vac.is_visible_css_selectop(self.driver, locator)
        return ele

    def _visible_css_selectop(self, locator, timeout=5):
        # 判断元素是否存在，如果存在就进行点击
        self.vac.css_click(self.driver, locator)
        pass

    def _visible_css_selectop_text(self, locator):
        # 判断元素是否存在，如果存在就进行获取元素的text属性
        _text = self.vai._visible_selectop_text(self.driver, locator)
        return _text

    def _visible_css_selectop_attribute(self, locator, attr="value"):
        # 判断元素是否存在，如果存在就获取元素的value属性内容
        _attribute = self.vai._visible_selectop_attribute(self.driver, locator, attr)
        return _attribute

    def _visible_css_selectop_Id(self, locator):
        # 判断元素是否存在，如果存在就获取元素的value属性内容
        _attribute = self.vai._visible_selectop_id(self.driver, locator, "disabled")
        return _attribute

    def _sendKeys_css_selectop(self, locator, content):
        # 判断元素是否存在，如果存在就进行输入
        self.vai.css_input(self.driver, locator, content)

    def _visible_json_click(self, locator):
        # 通过元素id利用js进行点击
        self.vac.id_confirm_prompt(self.driver, locator)

    def _visible_json_input(self, ordinal, parameter):
        # 利用js通过元素id直接修改value的数据
        self.vai.id_js_input(self.driver, ordinal, parameter)

    def _visible_json_save(self, ordinal, parameter):
        # 利用js通过元素id直接修改value的数据
        self.vai.id_js_cursor_save(self.driver, ordinal, parameter)

    """
        #--------------------单选框按钮的点击-----------------------------------------
    """

    def visibleRadioSelected(self, check, status):
        """
        当单选框在页面的状态跟期望的不一致时，会执行点击动作。
        相反则不执行点击动作
        status为False时表示期望单选框为不选中状态
        相反则表示选中状态
        :param check:  需要点击的单选框
        :param status:  期望单选的状态，默认为False
        :return:
        """
        print("单选框不用进行点击") if operator.eq(check.is_selected(), status) else self.vac.element_click(check)  # 元素点击

    """
        #--------------------数据库查询-----------------------------------------
    """

    def create_database(self):
        """
        数据库查询及内容返回
        :return:  返回查询到的内容
        """
        pm = pymysqls()
        pm.connects_readModel()

        return pm

    def mysql_single_selects(self, sql):
        pm = self.create_database()
        print("sql --------> {}".format(sql))
        result = pm.single_cross_selects(sql)
        pm.closes()

        return result

    def mysqlTotalSelects(self, sql):
        pm = self.create_database()
        result = pm.total_vertical_selects(sql)
        pm.closes()

        return result

    """
    #--------------------json数据的转换-----------------------------------------
    """

    def strTodict(self, title):
        print("需要转化你json数据--> %s" % title)
        return json.loads(title) if title is not None else "json中loads错误了"

    """
    #--------------------其他一些配置部分-----------------------------------------
    """

    def sleep_time(self, times=1):
        time.sleep(times)

    def abnormal_exit(self, msg: str = "页面没有数据"):
        try:
            sys.exit(0)
        except:
            print("%s ,程序强制退出" % msg)

    def error_log(self, function):
        # 执行文件的文件名
        basename = os.path.splitext(os.path.basename(__file__))[0]

        # 拼接名字
        name_tion = basename + "_" + function

        # 调用错误类
        dError.error_output(name_tion, self.driver)

    def _start_thread_pool(self, funktion):  # 开启线程池
        # funktion = [ap._excel_Data, get_basename]  # 该列表存放需要执行的函数
        # print("Opening thread execution %s" % time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
        # faden = []  # 该列表存放已经开启的线程
        #
        # inhalt = []  # 该列表存放线程中所执行的函数返回值内容
        #
        # for para in funktion:  # 遍历函数开启线程
        #     threads = th(para)
        #     faden.append(threads)
        #     threads.start()
        #
        # for argu in faden:  # 开启的线程中，进行阻塞，当子线程完成之后才继续下一步
        #     argu.join()
        #     inhalt.append(argu.get_result())
        #
        # # overall_ExcelData = inhalt[0]  # df转换的数据，方便对excel进行操作r
        # print("Thread execution finished %s" % time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
        # return inhalt
        pass


if __name__ == '__main__':
    co = ComparedVerify()
    excelData = co._excel_Data('discount', 1)

    # 获取excel路径
    # file_path = readModel.establish_con(model="excelmodel").get("excel", 'discount')
    # # 读取相应路径中的数据
    # read = OpenExcelPandas(file_path,1)
    # excelData = read.readCaseExcel()

    print(excelData)
