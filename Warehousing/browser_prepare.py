# -*- coding: utf-8 -*-
"""
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
@author:    ln_company
@license:   (C) Copyright 2016- 2018, Node Supply Chain Manager Corporation Limited.
@Software:  PyCharm
@file:      browser_prepare.py
@time:      2018/12/17 16:45
@desc:      浏览器工作
"""
import os

from selenium import webdriver
from selenium.common.exceptions import WebDriverException


class BrowserPrepare(object):
    """
    工作内容:
    1. 打开浏览器
    2. 执行元素校验 = [click,input,visible]
    """

    def __init__(self, driver_browser='chrome'):
        # 创建浏览器对象
        if 'chrome' == driver_browser or 'Chrome' == driver_browser:
            self.chrome_browser()
        elif 'firefox' == driver_browser or 'Firefox' == driver_browser:
            self.firefox_browser()
        else:
            self.ie_browser()

        self.browser.maximize_window()
        # 输入网址
        self.browser.get(url)
        # 等待网页加载，加载时间为10s，加载完就跳过
        # 隐形等待时间和显性等待时间不同时，默认使用两者之间最大的那个
        self.browser.implicitly_wait(15)
        pass

    def chrome_browser(self):
        """
        调用函数，实现打开谷歌浏览器的步骤
        :return:
        """
        self.browser = webdriver.Chrome(executable_path=os.path.join(driver_path, 'chromedriver239-68.exe'))

    def ie_browser(self):
        """
        调用函数，实现打开ie浏览器的步骤
        :return:
        """
        # https://www.cnblogs.com/ppppying/p/6143658.html
        # 实现全局变量的引用
        self.browser = webdriver.Ie(executable_path=os.path.join(driver_path, 'IEDriverServer.exe'))
        self.BROWSER_NAME = "IE浏览器"

    def firefox_browser(self):
        """
        调用函数，实现打开火狐浏览器的步骤
        :return:
        """

        # 实现全局变量的引用
        firefoxBin = os.path.abspath(r"E:\Program Files\Mozilla Firefox\firefox.exe")
        os.environ["webdriver.firefox.bin"] = firefoxBin
        self.BROWSER_NAME = "火狐浏览器"
        # 代码加载火狐驱动
        firefoxgeckobdriver = os.path.abspath(os.path.join(driver_path, 'geckodriver64.exe'))
        self.browser = webdriver.Firefox(options, executable_path=firefoxgeckobdriver)

    def mobile_phone_mode(self):
        '''
        Set the Google browser to mobile mode
        :return:
        '''
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

    def chrome_prefs_flash(self):
        '''
        When the Google browser runs, flash is not loaded
        :return:
        '''
        from selenium.webdriver.chrome.options import Options

        prefs = {
            "profile.managed_default_content_settings.images": 1,
            "profile.content_settings.plugin_whitelist.adobe-flash-player": 1,
            "profile.content_settings.exceptions.plugins.*,*.per_resource.adobe-flash-player": 1
        }

        options = Options()
        options.add_experimental_option("prefs", prefs)
        return options

    def firefox_prefs_flash(self):
        '''
        When firefox runs, flash is not loaded
        :return:
        '''
        options = webdriver.FirefoxProfile()
        # 其中plugin.state.flash后的数值可以为0,1,2； 0：禁止，1：询问，2：允许。
        options.set_preference("plugin.state.flash", 2)
        return options
