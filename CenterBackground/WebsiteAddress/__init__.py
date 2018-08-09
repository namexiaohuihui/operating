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
@author: 70486
@license: (C) Copyright 2016- 2018, Node Supply Chain Manager Corporation Limited.
@software: PyCharm
@file: __init__.py.py
@time: 2018/7/30 17:07
@desc:
'''
from CenterBackground.judgmentVerification import JudgmentVerification


class WebsiteCoexistence(JudgmentVerification):
    # 该菜单在所属目录的绝对位置
    CHILD_TAGS_LOCATION = "9"

    # 该菜单的用例所处位置的总目录
    MODEI_KEY_POSITION = "还没写"

    def _rou_system(self):
        """
        进入菜单下面的子目录
        :return:  暂时没有返回值
        """
        self.father_tags = self.CHILD_TAGS_LOCATION
        self.child_tags = self.FATHER_TAGS_LOCATION
        self._rou_background()
        pass

    def content_header_title(self, basename) -> '临时函数到时候去除':
        # 获取页面标题
        sidebar_title = self._visible_css_selectop_text(self.sidebar)
        content_title = self._visible_css_selectop_text(self.content_header)
        print("%s 进入页面成功" % basename) if sidebar_title == content_title else print("%s 进入页面失败" % basename)
