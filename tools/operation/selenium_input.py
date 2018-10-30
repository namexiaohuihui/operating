# -*- coding: utf-8 -*- 
"""
@__author__ :70486 
@file: selenium_input.py
@time: 2017/6/21 0:01
"""
# 这是元素输入类，传入相应的id，name，text，xpath，css以及内容就可以执行输入的指令
from tools.operation.selenium_visible import action_visible

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


class action_input(action_visible):
    def id_input(self, browser, id, parameter):
        ele = self.is_visible_id(browser, id)
        if ele != False:  # 判断是否出现
            # 元素输入
            self.ele_clear_keys(ele, parameter)
        else:
            self.error_log(browser)

    def name_input(self, browser, name, parameter):
        ele = self.is_visible_name(browser, name)
        if ele != False:  # 判断是否出现
            # 元素输入
            self.ele_clear_keys(ele, parameter)
        else:
            self.error_log(browser)

    def css_input(self, browser, css, parameter, timeout=5):
        ele = self.is_visible_css_selectop(browser, css)
        if ele != False:  # 判断是否出现
            # 元素输入
            self.ele_clear_keys(ele, parameter)
        else:
            self.error_log(browser)

    def css_input_number(self, browser, css, parameter, number=0):
        """
        指定元素组中,某个元素的动作
        :param browser: 浏览器对象
        :param css: cssSelectop
        :param parameter: 输入的信息
        :param number: 返回元素组中,指定位置的元素
        :return:
        """
        ele = self.is_visibles_css_selectop(browser, css)
        if ele != False:  # 判断是否出现
            # 元素输入
            if number <= len(ele):
                self.ele_clear_keys(ele[number], parameter)
            else:
                raise Exception("元素组的长度超标: css_input_number")
        else:
            self.error_log(browser)

    def xpath_input(self, browser, xpath, parameter):
        ele = self.is_visible_xpath(browser, xpath)
        if ele != False:  # 判断是否出现
            # 元素输入
            self.ele_clear_keys(ele, parameter)
        else:
            self.error_log(browser)

    def transmitList(self, browser, combination):
        # 对集合里面的元素执行遍历输入
        for num in range(len(combination)):
            meter = combination[num]
            self.css_input(browser, meter.parameter, meter.content)

    def transmitDictionaries(self, browser, combination):
        # 对列表里面的元素执行遍历输入
        for _key, _value in combination.items():
            self.css_input(browser, _value, _key)

    def ele_js_cursor_save(self, browser, ordinal, parameter):
        """
        先通过css找到元素,之后在通过JS对value进行写入
        :param browser: 浏览器对象
        :param ordinal: 需要写入元素的路径
        :param parameter: 需要输入的对象
        :return:
        """
        try:
            ordinal = self.is_visible_css_selectop(browser, ordinal)
            browser.execute_script("\'" + ordinal + "\'.value=\'" + parameter + "\';")
            self.sleep_Rest()
        except:
            self.error_log(browser)

    def id_js_input(self, browser, ordinal, parameter: str):
        """
        通过js找到相应的id对象并对其进行输入操作
        1.光标选择需要输入value的对象
        2.执行js输入
        3.光标从已选择的对象移出
        :param browser: 浏览器对象
        :param ordinal: 需要执行输入的对象
        :param parameter: 输入的value
        :return:
        """
        try:
            self.focus_id(browser, ordinal)
            self.id_js_cursor_save(browser, ordinal, str(parameter))
            self.blur_id(browser, ordinal)
        except:
            self.error_log(browser)

    def id_js_cursor_save(self, browser, ordinal, parameter):
        # 通过id进行js输入
        try:
            browser.execute_script("document.getElementById(\'" + ordinal + "\').value=\'" + parameter + "\';")
            self.sleep_Rest()
        except:
            self.error_log(browser)

    def css_js_cursor_save(self, browser, ordinal, parameter):
        try:
            self.sleep_Rest()
            browser.execute_script("document.querySelector(\'" + prompt + "\').value=\'" + parameter + "\';")
        except Exception as a:
            function = inspect.stack()[0][3]  # 执行函数的函数名
            print("%s :没有找到这个元素: %s \n %s" % (function, ordinal, a))

    def blur_ele(self, browser, ele):
        # 光标从ele元素上移除
        browser.execute_script("arguments[0].blur();", ele)

    def blur_id(self, browser, ordinal):
        # 根据id从该元素上进行移除
        browser.execute_script("document.getElementById(\'" + ordinal + "\').blur();")
        self.sleep_Rest(0.5)

    def focus_id(self, browser, ordinal):
        # 防止找不到元素对象,加个延迟
        self.sleep_Rest(0.5)
        # 光标移动到id为ordinal的元素上
        browser.execute_script("document.getElementById(\'" + ordinal + "\').focus();")

    def focus_ele(self, browser, ele):
        # 光标移动到ele元素上
        browser.execute_script("arguments[0].focus();", ele)

    def differentiate_ele_input(self, browser, case_info, ordinal):
        info_bool = True
        if case_info['ele'] == 'id':
            self.id_input(browser, ordinal, case_info["parameter"])
            pass
        elif case_info['ele'] == 'css':
            self.css_input(browser, ordinal, case_info["parameter"])
            pass
        else:
            print("ele_input_and_mode在css中没有css找到way")
            info_bool = False
            pass
        return info_bool

    def differentiate_js_input(self, browser, case_info, ordinal):
        info_bool = True
        if case_info['ele'] == 'id':
            self.id_js_input(browser, ordinal, case_info["parameter"])
            pass
        elif case_info['ele'] == 'css':
            self.css_js_cursor_save(browser, ordinal, case_info["parameter"])
            pass
        else:
            print("ele_input_and_mode在js中没有找到way")
            info_bool = False
            pass
        return info_bool

    def ele_input_and_mode(self, browser, case_info, ordinal):
        """
        判断相应的元素类型来执行动作
        :param browser: 浏览器对象
        :param case_info: 需要判断的数据
        :param ordinal: 元素路径
        :return:
        """
        case_info = case_info
        info_bool = False  # 检验程序是否需要执行下去

        if case_info['way'] == 'js':
            info_bool = self.differentiate_js_input(browser, case_info, ordinal)

        elif case_info['way'] == 'css':
            info_bool = self.differentiate_ele_input(browser, case_info, ordinal)

        else:
            print("ele_input_and_mode在way中没有数据信息")
            pass

        # 删除这个参数
        del case_info
        return info_bool

    def ele_clear_keys(self, ele, parameter):
        # 执行输入的操作
        ele.clear()
        ele.send_keys(parameter)
        self.sleep_Rest()
