# -*- coding: utf-8 -*- 
"""
@__author__ :70486 
@file: ExclusiveOperation.py
@time: 2017/12/20 22:49
@项目名称:operating
"""
import selenium.webdriver.support.expected_conditions as EC
import selenium.webdriver.support.ui as ui
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.touch_actions import TouchActions
from practical.config import readModel
from practical.utils.OpenpyxlExcel import READEXCEL, PANDASDATA


class exclusiveoperation(object):
    def setStart(self):
        self.sign_browser()  # 打开浏览器

    def setStop(self):
        pass

    def sign_browser(self):
        """
        打开浏览器的步骤
        :return:
        """
        from practical.constant.browser_establish import browser_confirm
        # 1.创建浏览器所在函数的对象
        bc = browser_confirm.__new__(browser_confirm)
        options = bc.mobile_phone_mode()

        conf = readModel.establish_con()
        url = conf.get("wap", "url")
        # 2.调用已经规划好的浏览器函数
        self.driver = bc.url_opens(url, options)

        # 账号密码输入
        # self.sign_username(bc)

    def sign_username(self, bc, conf=None):
        """
        从配置文件中读取登陆名和密码
        :param bc:
        :param conf:
        :return:
        """
        if not conf: conf = readModel.establish_con()
        account = conf.get("username", "account")
        password = conf.get("username", "assword")
        bc.case_browesr(account, password)

    def sign_switching_logon(self, account, password):
        """
        点击登陆之后，进行输入账号密码及切换登陆页面的事务
        :param account:
        :param password:
        :return:
        """
        try:
            # 点击登陆按钮
            self.is_visible_css_selectop('.btn>a:nth-child(1)')

            self.is_visible_css_selectop('.login-type>a:nth-child(1)')  # 切换登陆方式

            # 账号密码的输入
            self.driver.execute_script("document.getElementById('J_tel').value=" + account + ";")
            self.driver.find_element_by_css_selector("#J_pwd").send_keys(password)

            # 登陆按钮
            self.driver.find_element_by_css_selector(".u-btn.u-btn-morange").click()

            # 获取登录的提示语
            text = self.is_visible_css_selectop_text('.toast-cont')
            self.log.info("登陆时提示内容： %s" % text)

            # 储存登陆之后的提示
            from PageWeb.WebEven.PersonalCenter.ExclusiveService.TemporaryData import temporarystorage
            temporarystorage().set_remarks(text)

        except Exception as message:
            function = inspect.stack()[0][3]  # 执行函数的函数名
            self.error_log(function, message)
            raise

    def add_goods(self):
        """
        选择商品并进行点击
        :return:
        """
        self.is_visible_css_selectop('.J_add.shop-goods-add.icon-font.icon-plus-str')
        self.sleep_Rest(2)

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

    def sleep_Rest(self, ti=2):  # 延迟
        import time
        time.sleep(ti)

    def get_size(self):
        # 获取浏览器的大小
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        return (x, y)

    def Interface_sliding(self):

        # 实行上下滑动的效果
        screen = self.get_size()

        x1 = screen[0] * 0.5
        y1 = screen[1] * 0.75

        cart_cont = self.driver.find_element_by_css_selector('.m-cart-cont')

        # 从指定的元素开始滑动
        # TouchActions(self.driver).scroll_from_element(cart_cont, x1, y1).perform()
        TouchActions(self.driver).scroll(x1, y1).perform()

    def touchActions_tap(self, element):
        # 点击元素
        TouchActions(self.driver).tap(element).perform()

    def is_visible_css_selectop(self, locator, timeout=10):
        # 一直等待某元素可见，默认超时10秒
        try:
            import datetime
            ui.WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((By.CSS_SELECTOR, locator)))
            element = self.driver.find_element_by_css_selector(locator)  # 创建元素对象
            self.touchActions_tap(element)
            return element
        except TimeoutException:
            print("元素未出现：   %s" % locator)
            return False

    def is_visible_css_selectop_text(self, locator, timeout=10):
        # 一直等待某元素可见，默认超时10秒
        try:
            import datetime
            ui.WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((By.CSS_SELECTOR, locator)))
            text = self.driver.find_element_by_css_selector(locator).text  # 创建元素对象
            return text
        except TimeoutException:
            print("元素未出现：   %s" % locator)
            return False

    def error_log(self, function, message):
        # 执行文件的文件名
        basename = os.path.splitext(os.path.basename(__file__))[0]

        # 拼接名字
        name_tion = basename + ":" + function

        # 调用错误类
        from practical.utils.DefinitionError import definition_error
        definition_error().error_output(name_tion, message, self.browser)
