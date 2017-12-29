# -*- coding: utf-8 -*- 
"""
@__author__ :70486 
@file: web_ToSign.py
@time: 2017/12/20 23:07
@项目名称:operating
"""
import os
import unittest

from practical.utils.logger import Log
from practical.config import readModel
from practical.utils.OpenpyxlExcel import READEXCEL,PANDASDATA

class signtoyou(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        # 该类运行时优先调用的函数
        basename = os.path.splitext(os.path.basename(__file__))[0]
        self.log = Log(basename)
        self.log.info("The program begins to execute. Don't stop me when you start.")
        # self.setStart(self)

    @classmethod
    def tearDownClass(self):
        # 该类结束时最后调用的函数
        self.log.info("Make it complete and continue to press it next time...")

    def sign_one(self, function, account=None, password=None):
        self.sign_browser()

        from PageWeb.WebEven.Auxiliary.OtherSign import user_sign
        user_sign(self.driver).sign_in(function,account, password)

    def sign_browser(self):
        from practical.constant.browser_establish import browser_confirm
        # 1.创建浏览器所在函数的对象
        bc = browser_confirm.__new__(browser_confirm)
        options = bc.mobile_phone_mode()

        conf = readModel.establish_con()
        url = conf.get("wap", "url")
        # 2.调用已经规划好的浏览器函数
        self.driver = bc.url_opens(url, options)

    def excel_Data(self, file_path=None):
        """
        从excel表格中获取数据并进行点击
        :param file_path:
        :return:
        """
        # 获取excel路径
        if file_path == None: file_path = readModel.establish_con().get("excel", "file")

        # 读取相应路径中的数据
        read = READEXCEL(file_path)

        # 获取case
        whole = read.position_sheet_row_value()
        # 获取内容
        row_col_data = whole[0]  #
        # 获取标题
        title_data = whole[1]

        # 数据转换
        pan = PANDASDATA(row_col_data)
        df = pan.definition_DataFrame(index="2017-12-24", periods=len(tuple(row_col_data)), columns=title_data)

        return df, row_col_data

    def save_csv(self, df, file_path="wenhao.csv"):
        # 保存df的数据
        df.to_csv(file_path, index=False, encoding="gbk")

    def test_ShoppingCart_login(self):
        """
        1.选择商品
        2.去结算
        :return:
        """
        excel = self.excel_Data()
        df = excel[0]
        row_col_data = excel[1]

        for number in range(len(row_col_data) - 1, len(row_col_data)):
            self.log.info("%s 开始执行" % df.iloc[number]["函数"])

            string = df.iloc[number]["输入"].split(',')
            account = string[0].split(':')[1]
            password = string[1].split(':')[1]

            self.sign_one(df.iloc[number]["函数"], account=account, password=password)

            from PageWeb.WebEven.Auxiliary.TemporaryData import temporarystorage
            df.iloc[number]["场景"] = temporarystorage().get_remarks()

            self.log.info("%s ： 执行完毕" % df.iloc[number]["场景"])

            # self.save_csv(df)  # 将数据进行保存


if __name__ == '__main__':
    unittest.main()
