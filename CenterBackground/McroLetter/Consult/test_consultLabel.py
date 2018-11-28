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
@file:      test_consultLabel.py
@time:      2018/9/19 16:43
@desc:
"""
import os
import inspect
import unittest
from CenterBackground import McroLetter
from CenterBackground.surfacejude import SurfaceJude
from tools.excelname.Center.mcroletterwechat import McroLetterWechat

basepath = os.path.split(os.path.dirname(__file__))[1]
basename = os.path.splitext(os.path.basename(__file__))[0]
basename = basepath + "-" + basename

# 传入子集的key，以及Excel文档中的sheet名字
config = McroLetter.add_key(McroLetter.consult, McroLetter.page)
c_label = SurfaceJude(config, basename, McroLetterWechat)


class TestConsultLabel(unittest.TestCase):
    """
    页面展示项的标题
    """

    def setUp(self):
        # 打开浏览器，定义log日志。读取excle文档数据
        c_label.log.info("%s ---setup: 每个用例开始前后执行" % basename)
        c_label.openingProgram()
        c_label._rou_background()
        pass

    def tearDown(self):
        c_label.log.info("%s ---teardown: 每个用例结束后执行" % basename)
        c_label.driver.quit()
        pass

    def test_showTitle(self):
        c_label.setFunctionName(inspect.stack()[0][3])
        c_label.title_execute()
        pass

    @unittest.skip("test_showSurface 跳过,open_id错误导致页面无法正常显示出数据信息")
    def test_showSurface(self):
        c_label.setFunctionName(inspect.stack()[0][3])
        c_label.surface_execute()
        pass


if __name__ == '__main__':
    unittest.main(verbosity=2)