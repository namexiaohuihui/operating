# -*- coding: utf-8 -*-
'''
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
@file:      screeningjude.py
@time:      2018/8/28 10:55
@Site :     
@desc:
'''
import operator
from tools.screeningdrop import ScreeningDrop
from CenterBackground import Commodities

from CenterBackground.judeVerification import JudgmentVerification

# 时间元素的标签属性
_placeholder = 'placeholder'


class ScreeningJude(JudgmentVerification):
    def __init__(self, module, sheet, basename, centerName):
        '''
        定义模块数据信息
        :param module:   元素模块
        :param sheet:   用例标签名
        :param basename:  执行程序的文件名
        '''
        JudgmentVerification.__init__(self, Commodities.add_key(module, sheet), basename)
        self.bi = centerName()
        pass

    def create_select(self, direction: str) -> ScreeningDrop:
        '''
        创建操作select的对象
        :param direction:
        :return:
        '''
        op_se = ScreeningDrop(self.driver, direction)
        return op_se

    def button_formSub(self, att: str):
        '''
        根据按钮位置来进行点击
        :param att:  按钮所在位置的key值
        :return:
        '''
        attribute = self._visible_returns_selectop(self.financial[self.bi.yaml_formSub()])
        attribute = attribute[int(self.financial[att]) - 1]
        return attribute

    def searchExport(self):
        att = self.overall[self.bi.whole_keys()]
        op_str = self.button_formSub(att).text
        ov_str = self.overall[self.bi.whole_default()]
        assert operator.eq(op_str, ov_str), 'Obtain all options values incorrectly %s' % selectPath

    def value_options_jude(self, selectPath: str):
        '''
        根据指定的路径获取select下面的全部option值
        :param selectPath: 下拉框对象。
        :param information: 比较错误之后，抛出的信息。
        :return:
        '''
        op_se = self.create_select(self.financial[selectPath])
        # 获取全部的options
        op_str = op_se.options_to_str()
        ov_str = self.overall[self.bi.whole_including()]
        assert operator.eq(op_str, ov_str), 'Obtain all options values incorrectly %s' % selectPath
        pass

    def value_options_default(self, selectPath: str):
        '''
        根据指定的路径获取select下默认的option值
        :param selectPath:
        :param information:
        :return:
        '''
        op_se = self.create_select(self.financial[selectPath])
        op_str = op_se.getSelectedOptions()
        ov_str = self.overall[self.bi.whole_default()]
        assert operator.eq(op_str, ov_str), 'Option defaults are incorrect: %s' % selectPath
        pass

    def value_option_traverse(self, selectPath):
        '''

        :param selectPath: 元素的路径
        :return:
        '''
        selectPath = self.financial[selectPath]
        op_se = self.create_select(selectPath)
        op_list = op_se.getAllOptions()
        for value_str in op_list:
            # 设置option
            op_se.setSelectorText(value_str)
            # 点击搜索按钮
            self.button_formSub(self.bi.yaml_search()).click()
            # 重新設置text之後，界面會進行刷新此時driver對象也發生改變需要重新進行獲取
            op_se = op_se.setSelectData(selectPath)
            # 判断当前显示的option是否为设置的option
            op_str = op_se.getSelectedOptions()
            assert operator.eq(value_str, op_str), 'Error appearing when iterating click option :　%s ' % selectPath

    def attribute_value(self):
        '''
        找到指定元素对应属性的值
        :return:
        '''
        timePath = self.overall[self.bi.whole_keys()]
        timePath = self.financial[timePath]  # 元素路径
        op_str = self.vai._visible_selectop_attribute(self.driver, timePath, _placeholder)  # 将属性转成对象
        ov_str = self.overall[self.bi.whole_default()]
        assert operator.eq(ov_str, op_str), 'Error in time entry box :　%s ' % timePath
        pass
