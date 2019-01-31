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
@author:  ln_company
@license: (C) Copyright 2016- 2018, Node Supply Chain Manager Corporation Limited.
@software: PyCharm
@file: test_formGroup.py
@time: 2018/8/13 17:01
@desc:
'''
import os
import inspect
import unittest
from CenterBackground import GoodsManagement
from tools.excelname.Center.googsMana import CityGoodsPage
from CenterBackground.screeningjude import ScreeningJude


class TestFormGroup(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        basepath = os.path.split(os.path.dirname(__file__))[1]
        cls.basename = os.path.splitext(os.path.basename(__file__))[0]
        cls.basename = basepath + "-" + cls.basename

        # 传入子集的key，以及Excel文档中的sheet名字
        config = GoodsManagement.add_key(GoodsManagement.inventory, GoodsManagement.select)
        cls.form_group = ScreeningJude(config, cls.basename, CityGoodsPage)

        if "\\" in os.path.dirname(__file__):
            cls.method_path = os.path.dirname(__file__).split('\\', 2)[-1]
        elif "/" in os.path.dirname(__file__):
            cls.method_path = os.path.dirname(__file__).split('/', 2)[-1]
        pass

    def setUp(self):
        # 获取运行文件的类名
        self.form_group.log.info("%s ---setup: 每个用例开始前后执行" % self.basename)
        # 打开浏览器，定义log日志。读取excle文档数据
        self.form_group.openingProgram()
        self.form_group._rou_background()

    def tearDown(self):
        self.form_group.get_screenshot_image(method_obj=self)

        self.form_group.driver.quit()
        self.form_group.log.info("%s ---teardown: 每个用例结束后执行" % self.basename)
        pass

    def test_categorySelect(self):
        '''
        执行获取类目全部optios值的用例
        :return:
        '''
        self.form_group.setFunctionName(inspect.stack()[0][3])
        self.form_group.value_options_jude(selectPath=self.form_group.overall[self.form_group.bi.whole_keys()])
        pass

    def test_categoryDefault(self):
        '''
        执行类目默认值的用例
        :return:
        '''
        self.form_group.setFunctionName(inspect.stack()[0][3])
        self.form_group.value_options_default(selectPath=self.form_group.overall[self.form_group.bi.whole_keys()])
        pass

    def test_categoryTraverse(self):
        '''
        执行遍历选择类目中全部option值的用例
        :return:
        '''
        self.form_group.setFunctionName(inspect.stack()[0][3])
        self.form_group.value_option_traverse(formSub=self.form_group.bi.yaml_cityformSub(),
                                         selectPath=self.form_group.overall[self.form_group.bi.whole_keys()])
        pass

    # ----------------------关键字及按钮的位置----------------------
    def test_conditionsInput(self):
        self.form_group.setFunctionName(inspect.stack()[0][3])
        self.form_group.attribute_value()
        pass

    def test_button_search(self):
        self.form_group.setFunctionName(inspect.stack()[0][3])
        self.form_group.searchExport(formSub=self.form_group.bi.yaml_cityformSub())
        pass

    def test_button_export(self):
        self.form_group.setFunctionName(inspect.stack()[0][3])
        self.form_group.searchExport(formSub=self.form_group.bi.yaml_cityformSub())
        pass


if __name__ == '__main__':
    unittest.main(verbosity=2)
