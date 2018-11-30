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
@file:      test_uploadimg.py
@time:      2018/11/6 11:54
@desc:
"""
import os
import inspect
import unittest
from CenterBackground import GeneralizeAssist
from CenterBackground.GeneralizeAssist.Background.photograph import PhotoGraph
from tools.excelname.Center.generalize import Generalize
from CenterBackground import customTabs


class TestFocusTabs(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        basepath = os.path.split(os.path.dirname(__file__))[1]
        cls.basename = os.path.splitext(os.path.basename(__file__))[0]
        cls.basename = basepath + "-" + cls.basename
        # I pass in the key of the subset, and the sheet name in the Excel document
        config = GeneralizeAssist.add_key(GeneralizeAssist.img, GeneralizeAssist.page)
        cls.photo = PhotoGraph(config, cls.basename, Generalize)

    def setUp(self):
        # 获取运行文件的类名
        self.photo.log.info("%s ---setup: 每个用例开始前后执行" % self.basename)
        # 打开浏览器，定义log日志。读取excle文档数据
        self.photo.openingProgram()
        self.photo._rou_background()

    def tearDown(self):
        self.photo.driver.quit()
        self.photo.log.info("%s ---teardown: 每个用例结束后执行" % self.basename)
        pass

    def test_survivalTitle(self):
        """
        判断标题是否存在
        :return:
        """
        self.alert_click(inspect.stack()[0][3])
        box_title = self.photo.financial[self.photo.bi.yaml_box_title()]
        box_title = self.photo.vac.is_visible_css_selectop(self.photo.driver, box_title)
        assert box_title, "%s---没有读取到标题" % (self.photo.FUNCTION_NAME)
        pass

    def test_survivalImg(self):
        """
        判断图片是否存在
        :return:
        """
        self.alert_click(inspect.stack()[0][3])
        img_self.photo = self.photo.financial[self.photo.bi.yaml_img()]
        img_self.photo = self.photo.vac.is_visible_id(self.photo.driver, img_self.photo)
        assert img_self.photo, "%s---没有找到图片" % (self.photo.FUNCTION_NAME)
        img_self.photo = img_self.photo.get_attribute("src")
        self.photo.log.info("图片src属性值为:%s" % img_self.photo)
        pass

    def test_survivalSave(self):
        """
        判断按钮是否存在
        :return:
        """
        self.alert_click(inspect.stack()[0][3])
        img_save = self.photo.financial[self.photo.bi.yaml_img_save()]
        img_save = self.photo.vac.is_visible_id(self.photo.driver, img_save)
        assert img_save, "%s---提交按钮不见了" % (self.photo.FUNCTION_NAME)
        pass

    def alert_click(self, fun_name):
        """
        当提示flash没安装时,点击alert上面的确认按钮
        :param fun_name:
        :return:
        """
        dialog_box = self.photo.driver.switch_to_alert()
        print(dialog_box.text)
        dialog_box.accept()

        self.photo.setFunctionName(fun_name)
        self.photo.ti.dormancy_time(2)


if __name__ == '__main__':
    unittest.main(verbosity=2)
