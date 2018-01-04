# -*- coding: utf-8 -*- 
"""
@__author__ :70486 
@file: browser_establish.py
@time: 2017/6/20 22:24
"""
import os

from selenium import webdriver

from practical.constant.browser_into import browser_get_info
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

# __new__创建一个对象，__init__实例化一个对象
class browser_confirm(browser_get_info):
    # 单例类判断。如果该类创建过就不需要重新创建了
    def __new__(cls, *args, **kw):
        if not hasattr(cls, '_instance'):
            orig = super(browser_confirm, cls)
            cls._instance = orig.__new__(cls, *args, **kw)
        return cls._instance

    # 调用函数，实现打开谷歌浏览器的步骤
    def chrome_browser(self, options=None):
        try:
            self.browser = webdriver.Chrome(executable_path=r"E:\drivers\Drivers\chromedriver61-63.exe",
                                        chrome_options=options)
            print("打开谷歌")
            # 实现全局变量的引用
        except Exception as msg:
            self.writeLog(msg)
        return self.browser

    # 调用函数，实现打开ie浏览器的步骤
    def ie__browser(self):
        try:
            # 实现全局变量的引用
            self.browser = webdriver.Ie(r"E:\drivers\IEDriverServer.exe")
            print("打开IE")
        except:
            self.writeLog(self)
        return self.browser

    # 调用函数，实现打开火狐浏览器的步骤
    def firefox_browser(self):
        try:
            # 实现全局变量的引用
            firefoxBin = os.path.abspath(r"E:\Program Files\Mozilla Firefox\firefox.exe")
            os.environ["webdriver.firefox.bin"] = firefoxBin

            # 代码加载火狐驱动
            firefoxgeckobdriver = os.path.abspath(r"E:\drivers\Drivers\geckodriver64.exe")
            # os.environ["webdriver.path"] = firefoxgeckobdriver

            self.browser = webdriver.Firefox(executable_path=firefoxgeckobdriver)

            print("打开火狐")
        except Exception as msg:
            self.writeLog(msg)

        return self.browser

    # 运行浏览器
    def url_opens(self, url=None,options=None):

        print("浏览器开始执行初始化")

        # 创建浏览器对象
        self.browser = self.chrome_browser(options=options)
        self.browser.maximize_window()

        if url == None:
            # 输入网址
            # self.browser.get("C:\\Users\\70486\\Desktop\\youhui.html")
            # 　self.browser.get("C:\\Users\\70486\\Desktop\\－－ _ LIANNI.COM.html")
            # self.browser.get("C:\\Users\\Administrator\\Desktop\\youhui.html")
            self.browser.get('http://www.baidu.com')
        else:
            # 输入网址
            self.browser.get(url)

        # 等待网页加载，加载时间为10s，加载完就跳过
        self.browser.implicitly_wait(5)

        return self.browser;

    #   设置手机模式
    def mobile_phone_mode(self):
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
            self.writeLog('mobile_phone_mode')

