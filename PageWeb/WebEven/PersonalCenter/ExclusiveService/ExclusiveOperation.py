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

class exclusiveoperation(object):
    def setStart(self):
        self.sign_browser()  # 打开浏览器

    def setStop(self):
        pass

    def sign_browser(self):

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

    def sign_username(self, bc,conf=None):
        #　从配置文件中读取指定的数据
        if not conf:conf = readModel.establish_con()
        account = conf.get("username", "account")
        password = conf.get("username", "assword")
        bc.case_browesr(account, password)

    def sign_switching_logon(self,account,password):
        try:
            # 点击登陆按钮
            btn = self.is_visible_css_selectop('.btn>a:nth-child(1)')

            login = self.is_visible_css_selectop('.login-type>a:nth-child(1)')  # 切换登陆方式

            # self.driver.execute_script("document.getElementById('J_pwd').value=" + password + ";")
            self.driver.execute_script("document.getElementById('J_tel').value=" + account + ";")
            self.driver.find_element_by_css_selector("#J_pwd").send_keys(password)

            morange = self.driver.find_element_by_css_selector(".u-btn.u-btn-morange")  # 输入内容
            self.driver.execute_script("arguments[0].click();", morange)
            self.log.info("登陆时提示内容： %s" % self.is_visible_css_selectop('.toast-cont').text)  # 错误错误的原因
            from PageWeb.WebEven.PersonalCenter.ExclusiveService.TemporaryData import temporarystorage
            temporarystorage().set_remarks(self.is_visible_css_selectop_text('.toast-cont'))
        except Exception as message:
            function = inspect.stack()[0][3]  #　执行函数的函数名
            self.error_log(function,message)
            raise

    def add_goods(self):
        size = self.driver.find_elements_by_css_selector(".J_add.shop-goods-add.icon-font.icon-plus-str")
        self.driver.execute_script("arguments[0].click();", size[0])  # 找到商品并进行点击
        self.sleep_Rest(2)

    def excel_Data(self,file_path=None):
        if file_path==None:file_path = readModel.establish_con().get("excel", "file_path")
        read = READEXCEL(file_path)

        whole = read.position_sheet_row_value()  # 获取case
        row_col_data = whole[0]  #
        title_data = whole[1]

        pan = PANDASDATA(row_col_data)
        df = pan.definition_DataFrame(index="2017-12-24", periods=len(tuple(row_col_data)), columns=title_data)
        return df,row_col_data

    def save_csv(self,df,file_path = "wenhao.csv"):
        df.to_csv(file_path, index=False, encoding="gbk")

    def sleep_Rest(self, ti=2):  # 延迟
        import time
        time.sleep(ti)

    def get_size(self):  # 获取浏览器的大小
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

    def error_log(self,function,message):
        basename = os.path.splitext(os.path.basename(__file__))[0]  # 执行文件的文件名
        name_tion = basename + ":" + function
        from practical.utils.DefinitionError import definition_error
        definition_error().error_output(name_tion,message, self.browser)
