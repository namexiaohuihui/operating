# -*- coding: utf-8 -*- 
"""
@__author__ :70486 
@file: browser_establish.py
@time: 2017/6/20 22:24
"""
import os

from selenium import webdriver
from selenium.common.exceptions import WebDriverException

from tools import DefinitionErrors as dError

r'''
                       _oo0oo_
                      o8888888o
                      88" . "88
                      (| -_- |)
                      0\  =  /0
                    ___/`---'\___
                  .' \\|     |// '.
                 / \\|||  :  |||// \
                / _||||| -:- |||||- \
               |   | \\\  -  /// |   |
               | \_|  ''\---/''  |_/ |
               \  .-\__  '-'  ___/-. /
             ___'. .'  /--.--\  `. .'___
          ."" '<  `.___\_<|>_/___.' >' "".
         | | :  `- \`.;`\ _ /`;.`/ - ` : | |
         \  \ `_.   \_ __\ /__ _/   .-` /  /
     =====`-.____`.___ \_____/___.-`___.-'=====
                        `=---='


     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

               佛祖保佑         永无BUG
'''

driver_path = 'E:\drivers\Drivers'


# https://www.jianshu.com/p/82b0fdb5d2b8
# https://blog.csdn.net/chufazhe/article/details/51145834
# https://www.flash.cn/


# __new__创建一个对象，__init__实例化一个对象


class browser_confirm(object):
    BROWSER_NAME = ""

    # 单例类判断。如果该类创建过就不需要重新创建了
    def __new__(cls, *args, **kw):
        if not hasattr(cls, '_instance'):
            orig = super(browser_confirm, cls)
            cls._instance = orig.__new__(cls, *args, **kw)
        return cls._instance

    def single_browser(self):
        # 返回已经创建了的浏览器对象
        return self.browser

    # 调用函数，实现打开谷歌浏览器的步骤
    def chrome_browser(self, options=None):
        try:
            import sys
            self.browser = webdriver.Chrome(executable_path=os.path.join(driver_path, 'chromedriver.exe'))
            self.BROWSER_NAME = "无options的谷歌"
            # 实现全局变量的引用
        except WebDriverException as msg:
            self.writeLog()
        except Exception:
            self.writeLog()

    # 调用函数，实现打开ie浏览器的步骤
    def ie_browser(self):
        try:
            # https://www.cnblogs.com/ppppying/p/6143658.html
            # 实现全局变量的引用
            self.browser = webdriver.Ie(executable_path=os.path.join(driver_path, 'IEDriverServer.exe'))
            self.BROWSER_NAME = "IE浏览器"
            # print("打开IE")
        except:
            self.writeLog()

    # 调用函数，实现打开火狐浏览器的步骤
    def firefox_browser(self, options=None):
        try:
            # 实现全局变量的引用
            firefoxBin = os.path.abspath(r"E:\Program Files\Mozilla Firefox\firefox.exe")
            os.environ["webdriver.firefox.bin"] = firefoxBin
            self.BROWSER_NAME = "火狐浏览器"
            # 代码加载火狐驱动
            firefoxgeckobdriver = os.path.abspath(os.path.join(driver_path, 'geckodriver64.exe'))
            # os.environ["webdriver.path"] = firefoxgeckobdriver

            self.browser = webdriver.Firefox(options, executable_path=firefoxgeckobdriver)
        except Exception as msg:
            self.writeLog()

    # 运行浏览器
    def url_opens(self, url=None, liulanqi='chrome', options=None):
        # 创建浏览器对象
        if 'chrome' == liulanqi or 'Chrome' == liulanqi:
            self.chrome_browser(options)
        elif 'firefox' == liulanqi or 'Firefox' == liulanqi:
            self.firefox_browser(options)
        else:
            self.ie_browser()

        self.browser.maximize_window()
        # 输入网址
        self.browser.get(url)
        # 等待网页加载，加载时间为10s，加载完就跳过
        # 隐形等待时间和显性等待时间不同时，默认使用两者之间最大的那个
        self.browser.implicitly_wait(5)

        return self.browser

    def dingdong_mobile_opens(self, url):
        """
        打开谷歌并设置为手机模式,将浏览器对象进行返回操作
        :param url:
        :return:
        """
        options = self.mobile_phone_mode()
        self.url_opens(url, options=options)
        return self.single_browser()

    def mobile_phone_mode(self):
        '''
        谷歌设置手机模式
        Set the Google browser to mobile mode
        :return:
        '''
        try:
            from selenium.webdriver.chrome.options import Options
            # 有效的移动设备Galaxy S5.Nexus 5X.Nexus 6P
            # mobile_emulation = {"deviceName": "iPhone 7"}

            mobile_emulation = {
                "deviceMetrics": {"width": 360, "height": 640, "pixelRatio": 3.0},
                "userAgent": "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1"}

            # mobile_emulation = {"browserName": "IE"}
            options = Options()
            options.add_experimental_option("mobileEmulation", mobile_emulation)
            return options
        except:
            self.writeLog()

    def chrome_prefs_flash(self):
        '''
        谷歌禁止弹窗提示flash无法使用
        When the Google browser runs, flash is not loaded
        :return:
        '''
        try:
            from selenium.webdriver.chrome.options import Options

            prefs = {
                "profile.managed_default_content_settings.images": 1,
                "profile.content_settings.plugin_whitelist.adobe-flash-player": 1,
                "profile.content_settings.exceptions.plugins.*,*.per_resource.adobe-flash-player": 1
            }

            options = Options()
            options.add_experimental_option("prefs", prefs)
            return options
        except:
            self.writeLog()

    def firefox_prefs_flash(self):
        '''
        火狐禁止弹窗提示flash无法使用
        When firefox runs, flash is not loaded
        :return:
        '''
        try:
            options = webdriver.FirefoxProfile()
            # 其中plugin.state.flash后的数值可以为0,1,2； 0：禁止，1：询问，2：允许。
            options.set_preference("plugin.state.flash", 2)
            return options
        except:
            self.writeLog()

    def writeLog(self):
        basename = os.path.splitext(os.path.basename(__file__))[0]

        dError.error_mess(basename)


if __name__ == '__main__':
    bc = browser_confirm()
    bc.url_opens(r'C:\Users\DingDonf\Desktop\customer.htm')
    from bs4 import BeautifulSoup

    label_text = bc.browser.page_source
    soup = BeautifulSoup(label_text, "lxml")
    fatal_error = soup.br
    if fatal_error:
        fatal_error_pare = fatal_error.parent
        for i, child in enumerate(fatal_error_pare.children, start=1):
            if not child.name in ('div', 'table'):
                print(child, child.name)

    else:
        print("没有报错")
    bc.browser.quit()
