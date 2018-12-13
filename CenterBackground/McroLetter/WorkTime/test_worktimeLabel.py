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
@file:      test_inviteLabel.py
@time:      2018/9/19 16:43
@desc:
"""
import os
import inspect
import unittest
from CenterBackground import McroLetter
from CenterBackground.surfacejude import SurfaceJude
from tools.excelname.Center.mcroletterwechat import McroLetterWechat


class TestInviteLabel(unittest.TestCase):
    """
    页面展示项的标题
    """
    INVITE_DESIGNATED_TIME = "工作时间设置"
    INVITE_DESIGNATED_REPLY = "回复模式"

    @classmethod
    def setUpClass(cls):
        basepath = os.path.split(os.path.dirname(__file__))[1]
        cls.basename = os.path.splitext(os.path.basename(__file__))[0]
        cls.basename = basepath + "-" + cls.basename
        config = McroLetter.add_key(McroLetter.worktime, McroLetter.page)
        cls.wt_label = SurfaceJude(config, cls.basename, McroLetterWechat)
        cls.INVITE_DESIGNATED_TABS = cls.wt_label.bi.yaml_tabs()

    def setUp(self):
        # 获取运行文件的类名
        self.wt_label.log.info("%s ---setup: 每个用例开始前后执行" % self.basename)
        # 打开浏览器，定义log日志。读取excle文档数据
        self.wt_label.openingProgram()
        self.wt_label._rou_background()
        pass

    def tearDown(self):
        self.wt_label.driver.quit()
        self.wt_label.log.info("%s ---teardown: 每个用例结束后执行" % self.basename)
        pass

    def test_dorkingdays(self):
        """
        暂时只做简单的数据读取
        :return:
        """
        self.wt_label.setFunctionName(inspect.stack()[0][3])
        
        # 找到单选框对象的元素所在位置
        ele_check = self.wt_label.financial[self.wt_label.bi.yaml_wt_check()]
        # 根据路径找到元素
        ele_check = self.wt_label._visible_returns_selectop(ele_check)
        # 断言判断元素是否存在
        assert type(ele_check) != bool, "test_dorkingdays not Could checkout"
        # 遍历获取元素的text
        ele_check = list(map(lambda single: single.text, ele_check))
        # 输出text
        self.wt_label.log.debug("test_dorkingdays get is data : %s" % ele_check)
        pass

    def test_workingtime(self):
        """
        读取4个输入框是否存在
        :return:
        """
        # 读取函数名并执行切换操作
        self.wt_label.setFunctionName(inspect.stack()[0][3])
        self.wt_label.designated_box(self.INVITE_DESIGNATED_TABS, self.INVITE_DESIGNATED_TIME)
        # 读取开始时间和结束时间对象的所在位置
        ele_amstart = self.wt_label.financial[self.wt_label.bi.yaml_amstart()]
        ele_amsend = self.wt_label.financial[self.wt_label.bi.yaml_amsend()]
        ele_pmstart = self.wt_label.financial[self.wt_label.bi.yaml_pmstart()]
        ele_omstart = self.wt_label.financial[self.wt_label.bi.yaml_pmsend()]
        # 获取对象的value
        self.wt_get_attribute_value(ele_amstart, "ele_amstart")
        self.wt_get_attribute_value(ele_amsend, "ele_amsend")
        self.wt_get_attribute_value(ele_pmstart, "ele_pmstart")
        self.wt_get_attribute_value(ele_omstart, "ele_omstart")
        pass

    def test_replymode(self):
        self.wt_label.setFunctionName(inspect.stack()[0][3])
        self.wt_label.designated_box(self.INVITE_DESIGNATED_TABS, self.INVITE_DESIGNATED_REPLY)

        # 找到单选框对象的元素所在位置
        ele_check = self.wt_label.financial[self.wt_label.bi.yaml_wt_check()]
        # 根据路径找到元素
        ele_check = self.wt_label._visible_returns_selectop(ele_check)
        # 断言判断元素是否存在
        assert type(ele_check) != bool, "test_dorkingdays not Could checkout"
        # 遍历获取元素的text
        ele_check = list(map(lambda single: single.text, ele_check))
        # 输出text
        self.wt_label.log.debug("test_dorkingdays get is data : %s" % ele_check)

        pass

    def wt_get_attribute_value(self, am_pm, str_msg):
        am_pm = self.wt_label.vai.differentiate_element_exist(self.wt_label.driver, 'id', am_pm)
        am_pm = am_pm.get_attribute('value')
        assert type(am_pm) != bool, "test_workingtime is %s object judge error" % str_msg
        self.wt_label.log.debug("test_workingtime-%s data is %s" % (str_msg, am_pm))


if __name__ == '__main__':
    unittest.main(verbosity=2)
