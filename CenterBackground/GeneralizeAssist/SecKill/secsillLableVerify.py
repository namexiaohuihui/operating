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
@file:      SecKillLableVerify.py
@time:      2018/11/12 14:57
@desc:
"""
from CenterBackground.screeningjude import ScreeningJude


class SecKillLableVerify(ScreeningJude):
    """
    搜索按钮名字是单独独立的
    """
    def __init__(self, config, basename, centerName):
        '''
        定义模块数据信息
        :param module:   元素模块
        :param sheet:   用例标签名
        :param basename:  执行程序的文件名
        '''
        ScreeningJude.__init__(self, config, basename, centerName)
        pass

    def value_option_traverse(self, formSub, selectPath):
        '''
        遍历选择select之后点击搜索按钮
        :param selectPath: 元素的路径
        :return:
        '''
        selectPath = self.financial[selectPath]  # 找到指定标签的元素地址
        op_se = self.create_select(selectPath)
        op_list = op_se.getAllOptions()
        for value_str in op_list:
            # 设置option
            op_se.setSelectorText(value_str)

            # 点击搜索按钮
            att = self.overall[self.bi.whole_keys()]
            att = self.financial[att]
            self._visible_css_selectop(att)

            # 重新設置text之後，界面會進行刷新此時driver對象也發生改變需要重新進行獲取
            op_se = op_se.setSelectData(selectPath, self.attrEle)
            # 判断当前显示的option是否为设置的option
            op_str = op_se.getSelectedOptions()
            msg = 'Error appearing when iterating click option :　%s ' % selectPath
            self.debugging_log(value_str, op_str, msg)

    def searchExport(self, formSub):
        """
        读取指定元素的text与产品定义的是否一致
        :param formSub:
        :return:
        """
        att = self.overall[self.bi.whole_keys()]
        op_str = self._visible_css_selectop_text(self.financial[att])
        ov_str = self.overall[self.bi.whole_default()]
        self.debugging_log(op_str, ov_str, 'Obtain all options values incorrectly %s' % att)
