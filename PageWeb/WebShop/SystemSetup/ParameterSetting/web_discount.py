# -*- coding: utf-8 -*-
__author__ = 'Administrator'
"""
@file: web_goods_discount.py
@time: 2017/11/2 9:53
"""

import re
import time
import inspect
import unittest
from utils.Logger import Log
from PageWeb.WebShop.SystemSetup.ParameterSetting.discountOperationSteps import DiscountOperationSteps

"""
import的解释:
re:正则
time：时间
inspect :　获取函数名
unittest：用例框架
Log：log日志
DiscountOperationSteps ： 用例操作类

折扣页面:主要验证下面的问题:
1.小数
2.符合要求的数值
3.负数
4.特殊字符
5.中文
6.满足数值要求但符合要求

下文重复出现的内容注释：
1.@unittest.skip(r"跳过:XXXX") ：告诉unittest框架我要跳过这个用例，并打印出信息（跳过:XXXX）
"""

print("Start getting use cases : %s" % time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))

# 获取文件名
# basename = os.path.splitext(os.path.basename(__file__))[0]
# 定义类参数
# jv = JudgmentVerification()
# log = Log(basename)
# lpn = DiscountParameterNames()
# 读取数据内容
# overall_ExcelData = jv._excel_Data(filename="discount", SHEETNAME=1)
# 定义需要读取的文件名以及工作薄
print("Use case acquisition completion : %s" % time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))


class VerifyDiscount(unittest.TestCase):

    dis = DiscountOperationSteps()

    """
       继承函数
    """
    @classmethod
    def setUp(cls):
        # 该类运行时优先调用的函数
        # log.info("The program begins to execute. Don't stop me when you start.")
        basename = cls.__class__.__name__
        EXCLE_FILE= cls.dis.getDiscountExcle()
        cls.dis.openingProgram(basename,EXCLE_FILE)


    @classmethod
    def tearDown(cls):
        try:
            # 该类结束时最后调用的函数
            # log.info("Make it complete and continue to press it next time...")
            # jv.driver.quit()
            # overall_ExcelData.to_excel(basename + ".xlsx", index=False, encoding="gbk")
            pass
        except UnicodeDecodeError:
            log.info("又出现UTF-8的错误........")


    # ---------------用例部分-----------------
    @unittest.skip(r"跳过:test_city_number")
    def test_city_number(self):
        # 获取城市数量以及名字(编码)是否正确
        # 获取函数名
        self.dis.FUNCTION_NAME = inspect.stack()[0][3]
        self.dis._rou_fun()
        tags = self.dis.obtain_city_name()

        list_name = []
        list_attr = []
        for tag in tags:
            list_name.append(tag.text)
            attr = tag.get_attribute('href')
            regular = re.search(r'[1-9]\d{5}(?!\d)', attr)
            list_attr.append(int(regular.group()))

            self.dis._verify_content_mysql(list_name, list_attr)

    @unittest.skip(r"跳过:test_display_switch")
    def test_display_switch(self):
        # 判断显示项是否正确
        # 获取函数名
        self.dis.FUNCTION_NAME = inspect.stack()[0][3]
        self.dis._rou_fun()
        tags = self.dis.obtain_city_name()

        # 找到页面默认展示项的位置
        for tag in range(len(tags)):
            try:
                tags[tag].get_attribute('class')
                break
            except:
                pass

        # 跟需求上的展示项是否一致
        content = tags[tag] # 获取网页展示数据
        cont = self.dis.overall[lpn.ps_count_goods_discount()] # 获取数据库中的数据
        self.dis._verify_operator(content.text, cont) # 数据比较

        list_name = []
        list_attr = []
        for tag in range(len(tags)):
            jv.vac.element_click(tags[tag])  # 元素点击
            tags = self.dis.obtain_city_name()  # 点击之后会重新刷新页面，需要重新定位元素

            list_name.append(tags[tag].text)

            attr = jv.driver.current_url
            regular = re.search(r'[1-9]\d{5}(?!\d)', attr)
            list_attr.append(int(regular.group()))

        self.dis._verify_content_mysql(list_name, list_attr)

    @unittest.skip(r"跳过:test_display_switch")
    def test_cancel_input(self):
        """不设置优惠时对输入框进行校验"""
        # 获取函数名，并相应的目录下面
        self.dis.FUNCTION_NAME = inspect.stack()[0][3]
        self.dis._rou_fun()

        gd_check = self.dis._visible_return_selectop(lpn.goods_check)
        wa_check = self.dis._visible_return_selectop(lpn.watiki_check)
        # 单选框为选中状态就进行点击
        self.dis.visibleIsSelected(gd_check)
        self.dis.visibleIsSelected(wa_check)

        """通过输入框进行数据输入"""
        gd_dis = self.dis._visible_css_selectop_Id(lpn.goods_discount)
        gd_id = self.dis._visible_css_selectop_Id(lpn.goods_id)
        wa_dis = self.dis._visible_css_selectop_Id(lpn.watiki_discount)
        wa_id = self.dis._visible_css_selectop_Id(lpn.watikis_id)
        wa_max = self.dis._visible_css_selectop_Id(lpn.watikis_max)

        cancelInput = 'true' if gd_dis and gd_id and wa_dis and wa_id and wa_max else 'false';

        self.dis._verify_operator(cancelInput, self.overall[lpn.whole_result()])

    # @unittest.skip(r"跳过:test_all_cancel")
    def test_all_cancel(self):
        """不设置优惠直接提交"""
        # 获取函数名
        self.dis.FUNCTION_NAME = inspect.stack()[0][3]
        self.dis._rou_fun()

        # 执行单选框为选中状态时就进行点击的动作
        self.dis.isSelected()

        # 提交按钮的点击
        self.dis.visibleDiscountSave()

        # 执行弹窗的点击动作
        self.dis.promptVerification()

        # 比较数据库中的数据和输入的数据是否一致
        self.dis._verify_content_data()

    # @unittest.skip(r"跳过:test_all_choice")
    def test_all_choice(self):
        """设置优惠直接提交"""
        # 获取函数名
        self.dis.FUNCTION_NAME = inspect.stack()[0][3]
        self.dis._rou_fun()

        # 水单选框的点击以及信息输入
        self.dis.waterSelectedInput()

        # 水票单选框的点击以及信息输入
        self.dis.watikiSelectedInput()

        # 提交按钮的点击
        self.dis.visibleDiscountSave()

        # 执行弹窗的点击动作
        self.dis.promptVerification()

        # 数据库信息比较
        self.dis._verify_content_data()

    # @unittest.skip(r"跳过:test_water_NotInput")
    def test_water_NotInput(self):
        # 获取函数名
        self.dis.FUNCTION_NAME = inspect.stack()[0][3]
        self.dis._rou_fun()

        # 水单选框的点击以及信息输入
        self.dis.RADIO_STATUS = True
        self.dis.goodsCheckClick()
        self.dis.waterInput()

        # 提交按钮的点击
        self.dis.visibleDiscountSave()

        # 输入错误内容时，弹窗的提示
        self.dis.promptErrorInformation()


if __name__ == '__main__':
    unittest.main()
