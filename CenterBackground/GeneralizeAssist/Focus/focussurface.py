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
@file:      focussurface.py
@time:      2018/11/5 11:09
@desc:
"""
import time
import threading
from tools import StringCutting
from CenterBackground.surfacejude import SurfaceJude


class FocusSurface(SurfaceJude):

    def __init__(self, config, basename, centerName):
        '''
        定义模块数据信息
        :param module:   元素模块
        :param sheet:   用例标签名
        :param basename:  执行程序的文件名
        :param centerName:  元素所在的类
        '''

        SurfaceJude.__init__(self, config, basename, centerName)
        pass

    def traverseYield(self, thead_tr, tbody_class):
        '''
        :param thead_tr:  页面内容标题
        :param tbody_class:  页面内容展示项
        :return:
        '''
        _button = "button"
        _img = "img"
        _src = "src"
        for tr in tbody_class:
            tbody_tr = {}
            thead_length = len(thead_tr)
            len_bool = True
            for tr_len in range(thead_length):
                tr_td = tr.find_all('td')
                if len_bool and (1 is len(tr_td)):
                    tbody_tr[thead_tr[tr_len]] = tr_td[-1].text.replace(" ", "").replace("\n", "")
                    break
                    pass
                else:
                    if tr_len == thead_length - 1:  # 最后一个控件有多个按钮,需要单独处理
                        td_text = [td.text.replace(" ", "").replace("\n", "") for td in tr_td[tr_len].find_all(_button)]
                    elif tr_len == 1:  # 第二个对象为img，需要单独处理
                        td_text = tr_td[tr_len].find(_img)[_src]
                    else:
                        td_text = tr_td[tr_len].text.replace(" ", "").replace("\n", "")
                    tbody_tr[thead_tr[tr_len]] = td_text
                len_bool = False
            yield tbody_tr
        pass

    def surface_execute(self):
        # 负责储存读取的内容
        self.tbody_list = []

        # 对当前url进行切割
        current = self.driver.current_url

        # 2.获取页面内容的key
        thead_tr = self.success_execute()

        # 线程执行工作
        thread = threading.Thread(target=self.success_tbody, args=(current, thead_tr,))

        # 启动线程
        thread.setDaemon(True)
        thread.start()

        # 等待线程执行完成
        thread.join()

        import pprint
        pprint.pprint(self.tbody_list)

        pass
