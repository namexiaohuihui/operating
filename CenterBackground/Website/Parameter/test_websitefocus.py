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
@file:      test_addfocus.py
@time:      2018/11/6 11:03
@desc:
"""
import os
import inspect
import unittest
from CenterBackground import Website
from tools.excelname.Center.officialwebsite import OfficialWebsite
from CenterBackground.GeneralizeAssist.Invite.inviteoperatejude import InviteOperateJude


class TestOperateDelect(unittest.TestCase):
    """
    点击某个按钮,获取弹窗的标题
    """
    INVITE_DESIGNATED_BOX = "友情链接"

    @classmethod
    def setUpClass(cls):
        basepath = os.path.split(os.path.dirname(__file__))[1]
        cls.basename = os.path.splitext(os.path.basename(__file__))[0]
        cls.basename = basepath + "-" + cls.basename
        config = Website.add_key(Website.parameter, Website.add)
        cls.f_operate = InviteOperateJude(config, cls.basename, OfficialWebsite)
        cls.INVITE_DESIGNATED_TABS = cls.f_operate.bi.yaml_tabs()

        if "\\" in os.path.dirname(__file__):
            cls.method_path = os.path.dirname(__file__).split('\\', 2)[-1]
        elif "/" in os.path.dirname(__file__):
            cls.method_path = os.path.dirname(__file__).split('/', 2)[-1]
        pass

    def setUp(self):
        # 获取运行文件的类名
        self.f_operate.log.info("%s ---setup: 每个用例开始前后执行" % self.basename)
        # 打开浏览器，定义log日志。读取excle文档数据
        self.f_operate.openingProgram()
        self.f_operate._rou_background()
        pass

    def tearDown(self):
        self.f_operate.get_screenshot_image(method_obj=self)

        self.f_operate.driver.quit()
        self.f_operate.log.info("%s ---teardown: 每个用例结束后执行" % self.basename)
        pass

    def test_focus_home(self):
        self.f_operate.setFunctionName(inspect.stack()[0][3])
        ov_para = os.path.split(os.path.dirname(__file__))[0]
        self.f_operate.conditions_screening(ov_para)
        pass

    def test_focus_friendship(self):
        self.f_operate.setFunctionName(inspect.stack()[0][3])
        ov_para = os.path.split(os.path.dirname(__file__))[0]
        self.f_operate.conditions_screening(ov_para)
        pass


if __name__ == '__main__':
    unittest.main(verbosity=2)
