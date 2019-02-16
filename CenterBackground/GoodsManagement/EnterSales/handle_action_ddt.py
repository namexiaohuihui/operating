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
@file:      handle_action_ddt.py
@time:      2019/2/15 11:23
@desc:
"""
import os
import time

from tools.Logger import Log
from tools.YAMLconfig import readYaml
from tools.operation.selenium_click import action_click
from tools.operation.selenium_input import action_input
from tools.configs import readModel
from tools.browser_establish import browser_confirm
from CenterBackground import GoodsManagement


class HandleActionDdt(object):
    """
    打开浏览器
    定义日志信息
    配置元素路径对象
    """

    def __init__(self, basename, yaml_path):
        """
        实例化对象
        :param basename: 运行文件名
        :param yaml_path: 元素配置路径关键字所在的文件
        """
        self.basename = basename
        self.log = Log(self.basename)
        self.financial = readYaml.read_expression(yaml_path)

        self.a_click = action_click()
        self.a_input = action_input()
        pass

    def open_browser(self, option, liulanqi='chrome', options=None):
        # 打开浏览器
        bc = browser_confirm.__new__(browser_confirm)
        conf = readModel.establish_con(model="model")
        url = conf.get("wap", option)
        self.driver = bc.url_opens(url, liulanqi, options)
        pass

    def sigin_user_login(self, account, password):
        # 找到账号密码
        conf = readModel.establish_con(model="model")
        account = conf.get("username", account)
        password = conf.get("username", password)
        # 输入账号密码点击登录
        self.a_input.name_input(self.driver, 'username', account)
        self.a_input.name_input(self.driver, 'password', password)
        self.a_click.id_confirm_prompt(self.driver, "loginBtn")
        pass

    # -------------------------定义主菜单的所在位置------------------------
    def set_sidebar_number(self, number: int) -> None:
        '''通过number定义主菜单的所在位置'''
        self.sidebar = ".sidebar-menu>li:nth-child(%s)>.dropdown-toggle" % number

    def sidebar_number_get(self) -> "获取子菜单的所在位置":
        return self.sidebar

    # -------------------------定义子菜单的所在位置------------------------
    def set_treeview_number(self, number: int) -> "通过number定义子菜单的所在位置":
        '''通过number定义子菜单的所在位置'''
        self.treew = ".treeview-menu.menu-open>li:nth-child(%s)" % number

    def treeview_number_get(self) -> "获取子菜单的所在位置":
        return self.treew

    # -------------------通过第三方参数来设置或者读取主菜单的位置-------------
    father_tags = property(sidebar_number_get, set_sidebar_number, doc="Setting an error or getting the main menu.")

    # -------------------通过第三方参数来设置或者读取子菜单的位置
    child_tags = property(treeview_number_get, set_treeview_number, doc="Error setting or getting subtags.")

    def _rou_background(self):
        """
        father_tags： 定义菜单的所在位置
        child_tags ： 定义模块的所在位置
        :return:  暂时没有返回值
        """
        argument = GoodsManagement.get_argument_data()
        self.father_tags = argument['father']
        self.a_click.css_click(self.driver, self.father_tags)

        self.child_tags = argument[GoodsManagement.INVENTORY['module']]['child']
        self.a_click.css_click(self.driver, self.child_tags)

        pass

    def screen_set_up(self, url, account, password):
        """
        select用例中,需要执行的前置条件统一定义并进行调用
        :param basename: 文件名和类名的拼接对象
        :return:
        """
        # 获取运行文件的类名
        self.log.info("%s ---setup: 每个用例开始前后执行" % self.basename)
        # 打开浏览器，定义log日志。读取excle文档数据
        self.open_browser(url)
        self.sigin_user_login(account, password)
        self._rou_background()
        pass

    def screen_tear_down(self, perform_obj):
        """
        select用例中,需要执行的后置条件统一定义并进行调用
        :param perform_obj: 当前case运行的对象
        :return:
        """
        self.get_screenshot_image(method_obj=perform_obj)
        self.driver.quit()
        self.log.info("%s ---teardown: 每个用例结束后执行" % perform_obj.basename)
        pass

    def get_screenshot_image(self, method_obj):
        """
        执行保存截图功能
        :param method_obj: 当前运行文件主体
        :return:
        """
        # 判断执行是否出错
        bl_image_error = True
        for fun_name, error in method_obj._outcome.errors:
            if error:
                method_status = 'error'
                bl_image_error = False

        if bl_image_error:
            method_status = 'correct'

        method_obj.method_path = os.path.join(method_obj.method_path, method_status)

        method_name = "%s-%s.png" % (method_obj.basename.split("-")[-1], method_obj._testMethodName)

        # 获取年月日
        current_time = time.strftime('%Y-%m-%d', time.localtime())

        # 路径这块先这样写
        report_path = os.path.join(os.path.join(os.getcwd(), 'screenshots/imgs'), current_time)
        report_path = os.path.join(report_path, method_obj.method_path)

        # 文件保存路径不存在就创建
        if not os.path.exists(report_path): os.makedirs(report_path)

        file_path = os.path.join(report_path, method_name)
        print("截图" + file_path)

        # 截图保存
        self.driver.save_screenshot(file_path)

    def element_click_jump(self, ele_path):

        self.a_click.css_click(self.driver, self.financial[ele_path])
        pass

    def element_text(self, ele_path, text_title):
        ele_path = self.financial[ele_path]
        ele_text = self.a_input.is_visible_css_selectop(self.driver, ele_path).text
        assert ele_text == text_title, '跳转之后标题不对'
        pass
