# -*- coding: utf-8 -*-
__author__ = 'DingDong'
"""
@file: operationSelector.py
@time: 2018/4/10 11:17
"""
import time

from selenium.webdriver.support.select import Select

from tools.browser_establish import browser_confirm
from tools.operation.selenium_visible import action_visible


class OperationSelector(action_visible):
    # ----------------------------------初始化参数------------------------
    def __init__(self, drivers, labelPath=None):
        # 赋值浏览器
        self.drivers = drivers
        if labelPath:
            self.setSelectData(labelPath)

    def setSelectData(self, labelPath):
        # 找到select元素
        selectEle = self.is_visible_css_selectop(self.drivers, labelPath)
        self.select = Select(selectEle)
        # 装options的数据,不创建value的容器是因为很少使用value
        self.optionsList = []
        return self

    # --------------------------------参数类型转换----------------------
    def options_to_str(self):
        self.getAllOptions()
        str_option = ','.join(self.optionsList)
        return str_option

    # ----------------------------------获取参数------------------------

    def get_options(self):
        """
        统计options值，只限内部使用。外部不可调用
        :return:
        """
        for option in self.select.options:
            self.optionsList.append(option.text.strip())

    def get_value(self):
        """
        统计value值，只限内部使用。外部不可调用
        :return:
        """
        self.valueList = []
        for option in self.select.options:
            self.valueList.append(option.get_attribute("value").strip())

    def getSelector(self):
        # 　返回select对象
        return self.select

    def getSelectedOptions(self):
        # 返回当前业已选择的option
        selected = self.select.first_selected_option.text.strip()
        return selected

    def getAllOptions(self):
        """
        获取全部的option数据
        :return: 返回全部的option
        """
        if self.optionsList:
            pass
        else:
            self.get_options()
            pass
        return self.optionsList

    def getAllValue(self):
        """
        获取全部的value数据
        :return:  返回全部value
        """
        try:
            if self.valueList:
                pass
        except Exception as e:
            self.get_value()
            pass
        finally:
            return self.valueList

    def getOptionsSize(self):
        """
        先进options页面判断options数据是否存在
        然后在执行返回
        :return:  返回当前options值的总数
        """
        self.getAllOptions()
        return len(self.optionsList)

    def getValueSize(self):
        """
        先进去values页面判断values数据是否存在
        然后在执行返回
        :return: 返回当前options所对应的value值总数
        """
        self.getAllValue()
        return len(self.valueList)

    # ----------------------------------设置选择的参数------------------------
    def setSelectorValue(self, value):
        """
        通过value值来设置selector中的option
        :param value:  需要设置新的option值所对应的value
        :return: 返回替换前的option
        """
        selected = self.getSelectedOptions()
        self.select.select_by_value(value)
        return selected

    def setSelectorIndex(self, index):
        """
        通过index值来设置selector中的option
        :param index: 需要设置新的option值所对应的index
        :return:  返回替换前的option
        """
        selected = self.getSelectedOptions()
        self.select.select_by_index(index)
        return selected

    def setSelectorText(self, text):
        """
        通过text值来设置selector中的option
        :param text: 需要设置新的option值所对应的text
        :return: 返回替换前的option
        """
        try:
            selected = self.getSelectedOptions()
            if selected == text:  # 判断当前业已的option是否为需要新设置的数据信息
                pass
            else:
                self.select.select_by_visible_text(text)
        except:
            print("This parameter is not found in the drop-down box %s" % text)
        finally:
            return selected
    # ---------------------------------------遍历设置option值-----------------------------
    def traverseYield(self, textList):
        '''
        根据lit/dict创建迭代器
        :param textList:
        :return:
        '''
        for text in textList:
            yield text

    def traverseSetText(self, textList):
        '''
        通过lit/dict来设置select的option
        :param textList:
        :return:
        '''
        tr_yield = traverseYield(textList)
        for text in tr_yield:
            self.select.select_by_visible_text(text)

    # ----------------------------------取消已选择的参数------------------------
    def setDeselectAll(self):
        """
        取消select中全部业已选择的option
        :return: 返回取消前的option
        """
        selected = self.getSelectedOptions()
        self.select.deselect_all()
        return selected

    def setDeselectValue(self, value):
        """
        根据value来取消业已选择的option
        :param value: 取消option值所对应的value
        :return:返回取消前的option
        """
        selected = self.getSelectedOptions()
        self.select.deselect_by_value(value)
        return selected

    def setDeselectIndex(self, index):
        """
        根据index来取消业已选择的option
        :param index: 取消option值所对应的index
        :return:返回取消前的option
        """
        selected = self.getSelectedOptions()
        self.select.deselect_by_index(index)
        return selected

    def setDeselectText(self, text):
        """
        根据text来取消业已选择的option
        :param text: 取消option值所对应的text
        :return: 返回取消前的option
        """
        selected = self.getSelectedOptions()
        self.select.deselect_by_visible_text(text)
        return selected

    # -------------------------------根据新的label来设置内容------------------------------
    def lable_set_text(self, label, text):
        '''
        根据label来设置新的text
        :param label: select位置
        :param text:  需要设置的值
        :return:
        '''
        self.setSelectData(label)
        self.setSelectorText(text)
        time.sleep(0.5)


if __name__ == '__main__':
    from tools.operation.selenium_visible import action_visible

    be = browser_confirm()
    drivers = be.url_opens(r"F:\desktop\genghuan.html")
    # time.sleep(2)
    ele = action_visible().is_visible_css_selectop(drivers, '.form-control.staff')
    print(ele)
    ele.send_keys('55555555')
    # drivers.close()
