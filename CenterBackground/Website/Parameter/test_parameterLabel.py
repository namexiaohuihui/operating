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
@file:      test_focusLabel.py
@time:      2018/9/19 16:43
@desc:
"""
import os
import inspect
import unittest
from CenterBackground import Website
from CenterBackground.surfacejude import SurfaceJude
from tools.excelname.Center.officialwebsite import OfficialWebsite

basepath = os.path.split(os.path.dirname(__file__))[1]
basename = os.path.splitext(os.path.basename(__file__))[0]
basename = basepath + "-" + basename

# 传入子集的key，以及Excel文档中的sheet名字
config = Website.add_key(Website.parameter, Website.page)
p_page = SurfaceJude(config, basename, OfficialWebsite)


class TestParameterLabel(unittest.TestCase):
    """
    页面展示项的标题
    """
    INVITE_DESIGNATED_BOX = "友情链接"
    INVITE_DESIGNATED_TABS = p_page.bi.yaml_tabs()

    def setUp(self):
        # 打开浏览器，定义log日志。读取excle文档数据
        p_page.log.info("%s ---setup: 每个用例开始前后执行" % basename)
        p_page.openingProgram()
        p_page._rou_background()
        pass

    def tearDown(self):
        p_page.driver.quit()
        p_page.log.info("%s ---teardown: 每个用例结束后执行" % basename)
        pass

    def test_homeTitle(self):
        """
        页面标题
        :return:
        """
        p_page.setFunctionName(inspect.stack()[0][3])
        p_page.title_execute()
        pass

    def test_homeSurface(self):
        """
        页面内容
        :return:
        """
        p_page.setFunctionName(inspect.stack()[0][3])
        p_page.surface_execute()
        pass

    def test_friendshipTitle(self):
        """
        页面标题
        :return:
        """
        p_page.setFunctionName(inspect.stack()[0][3])
        p_page.designated_box(self.INVITE_DESIGNATED_TABS, self.INVITE_DESIGNATED_BOX)
        p_page.title_execute()
        pass

    def test_friendshipSurface(self):
        """
        页面内容
        :return:
        """
        p_page.setFunctionName(inspect.stack()[0][3])
        p_page.surface_execute()
        pass


if __name__ == '__main__':
    unittest.main(verbosity=2)
