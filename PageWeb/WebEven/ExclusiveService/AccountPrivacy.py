# -*- coding: utf-8 -*- 
"""
@__author__ :70486 
@file: AccountPrivacy.py
@time: 2018/1/4 22:13
@项目名称:operating
"""
import selenium.webdriver.support.expected_conditions as EC
import selenium.webdriver.support.ui as ui
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.touch_actions import TouchActions
from practical.utils.logger import Log
class account_privacy(object):

    def start_program(self,name):
        self.log = Log(name)
        self.log.info("The program begins to execute. Don't stop me when you start.")
        self.open_browser()
        self.sign_user_login()
        self.excel = self.excel_Data()

    def stop_program(self):
        self.log.info("Make it complete and continue to press it next time...")

    """
#------------------获取浏览器部分------------------------------------
    """
    def open_browser(self):
        from practical.constant.browser_establish import browser_confirm
        # 1.创建浏览器所在函数的对象
        bc = browser_confirm.__new__(browser_confirm)
        options = bc.mobile_phone_mode()

        from practical.config import readModel
        conf = readModel.establish_con()
        url = conf.get("wap", "url")

        # 2.调用已经规划好的浏览器函数
        self.driver = bc.url_opens(url, options)

    """
#------------------- 用户登录-------------------
    """

    def path_Route(self):
        self.is_visible_css_selectop(".nav-user")
        self.is_visible_css_selectop(".user-head")


    def sign_user_login(self, account, password):
        """
        不需要点击登录就可以直接进入登陆页面
        :param account:
        :param password:
        :return:
        """
        try:
            self.path_Route()

            self.is_visible_css_selectop('.login-type>a:nth-child(1)')  # 切换登陆方式

            # 账号密码的输入
            self.driver.find_element_by_css_selector("#J_tel").send_keys(account)
            self.driver.find_element_by_css_selector("#J_pwd").send_keys(password)

            # 登陆按钮
            self.is_visible_css_selectop(".u-btn.u-btn-morange")

            # 获取登录的提示语
            self.log.info("登陆提示信息-----> %s " % self.is_visible_css_selectop_text('.toast-cont'))

        except Exception as message:
            function = inspect.stack()[0][3]  # 执行函数的函数名
            self.error_log(function, message)
            raise

        """
#--------------------读取excel表格数据部分-----------------------------------------
        """

    def excel_Data(self, file_path=None):
        """
        从excel表格中获取数据并进行转换
        :param file_path:
        :return:
        """
        # 获取excel路径
        from practical.config import readModel
        if file_path == None: file_path = readModel.establish_con().get("excel", "exclusiveServiceFile"
                                                                                 "")

        # 读取相应路径中的数据
        from practical.utils.OpenpyxlExcel import READEXCEL, PANDASDATA
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

        """
#--------------------浏览器操作部分-----------------------------------------
        """

        def touchActions_tap(self, element):
            # 点击元素
            TouchActions(self.driver).tap(element).perform()
            self.sleep_Rest()

        """
#--------------------元素判断部分-----------------------------------------
        """

        def is_visible_css_selectop(self, locator, timeout=3):
            # 一直等待某元素可见，默认超时10秒
            try:
                import datetime
                # ui.WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((By.CSS_SELECTOR, locator)))
                element = ui.WebDriverWait(self.driver, timeout).until(
                    EC.visibility_of_element_located((By.CSS_SELECTOR, locator)))
                self.sleep_Rest(1)
                self.touchActions_tap(element)
                return element
            except TimeoutException:
                print("元素未出现：   %s" % locator)
                return False

        """
#--------------------其他一些配置部分-----------------------------------------
        """

    def sleep_Rest(self, ti=1):  # 延迟
        import time
        time.sleep(ti)

    def error_log(self, function, message):
        # 执行文件的文件名
        basename = os.path.splitext(os.path.basename(__file__))[0]

        # 拼接名字
        name_tion = basename + ":" + function

        # 调用错误类
        from practical.utils.DefinitionError import definition_error
        definition_error().error_output(name_tion, message, self.browser)
