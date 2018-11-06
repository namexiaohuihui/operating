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

# Path and file name splicing
basepath = os.path.split(os.path.dirname(__file__))[1]
basename = os.path.splitext(os.path.basename(__file__))[0]
basename = basepath + "-" + basename

# I pass in the key of the subset, and the sheet name in the Excel document
config = GeneralizeAssist.add_key(GeneralizeAssist.img, GeneralizeAssist.page)
photo = PhotoGraph(config, basename, Generalize)


class TestFocusTabs(unittest.TestCase):

    def setUp(self):
        # 打开浏览器，定义log日志。读取excle文档数据
        photo.openingProgram()
        photo._rou_background()
        print("%s ---setup: 每个用例开始前后执行" % basename)

    def tearDown(self):
        photo.driver.quit()
        print("%s ---teardown: 每个用例结束后执行" % basename)
        pass

    def test_survivalTitle(self):
        """
        判断标题是否存在
        :return:
        """
        self.alert_click(inspect.stack()[0][3])
        box_title = photo.financial[photo.bi.yaml_box_title()]
        box_title = photo.vac.is_visible_css_selectop(photo.driver, box_title)
        assert box_title, "%s---没有读取到标题" % (photo.FUNCTION_NAME)
        pass

    def test_survivalImg(self):
        """
        判断图片是否存在
        :return:
        """
        self.alert_click(inspect.stack()[0][3])
        img_photo = photo.financial[photo.bi.yaml_img()]
        img_photo = photo.vac.is_visible_id(photo.driver, img_photo)
        assert img_photo, "%s---没有找到图片" % (photo.FUNCTION_NAME)
        img_photo = img_photo.get_attribute("src")
        photo.log.info("图片src属性值为:%s" % img_photo)
        pass

    def test_survivalSave(self):
        """
        判断按钮是否存在
        :return:
        """
        self.alert_click(inspect.stack()[0][3])
        img_save = photo.financial[photo.bi.yaml_img_save()]
        img_save = photo.vac.is_visible_id(photo.driver, img_save)
        assert img_save, "%s---提交按钮不见了" % (photo.FUNCTION_NAME)
        pass

    def alert_click(self,fun_name):
        dialog_box = photo.driver.switch_to_alert()
        print(dialog_box.text)
        dialog_box.accept()

        photo.setFunctionName(fun_name)
        photo.ti.dormancy_time(2)



if __name__ == '__main__':
    unittest.main(verbosity=2)
