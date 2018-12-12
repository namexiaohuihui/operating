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
@file: inventoryLabelJude.py
@time: 2018/8/14 14:12
@desc:
'''

import time
import threading
from bs4 import BeautifulSoup
from tools import StringCutting
from CenterBackground.GoodsManagement import Inventory
from CenterBackground.judeVerification import JudgmentVerification
from tools.excelname.Center.gongsMana import CityGoodsPage


class InventoryLabelJude(JudgmentVerification):

    def __init__(self, config, basename, centerName):
        '''
        :param config: 头文件所在位置
        :param basename: 执行用例的文件名
        :param centerName: 参数定义的类对象
        '''
        JudgmentVerification.__init__(self, config, basename)
        self.bi = centerName()
        pass

    def bs4_soup(self):
        label_text = self.driver.page_source
        soup = BeautifulSoup(label_text, "lxml")
        return soup

    def traverseYield(self, thead_tr, tbody_class):
        '''

        :param thead_tr:  页面内容标题
        :param tbody_class:  页面内容展示项
        :return:
        '''
        for tr in tbody_class:
            tbody_tr = {}
            tr_td = tr.find_all('td')
            for tr_len in range(len(thead_tr)):
                if tr_len == len(thead_tr) - 1:
                    text = tr_td[tr_len].find('a').text
                    action = tr_td[tr_len].find('button')['data-action']
                    td_text = '%s %s' % (text, action)
                else:
                    td_text = str.strip(tr_td[tr_len].text)
                tbody_tr[thead_tr[tr_len]] = td_text
            yield tbody_tr

    def success_execute(self):
        soup = self.bs4_soup()
        thead_th = soup.find('tr').find_all('th')
        thead_tr = [str.strip(th.text) for th in thead_th]
        return thead_tr

    def success_tbody(self, url, thead_tr):
        self.driver.get(url)
        soup = self.bs4_soup()
        tbody_class = soup.find('tbody').find_all('tr')
        tr_yield = self.traverseYield(thead_tr, tbody_class)
        for text in tr_yield:
            self.tbody_list.append(text)

    # -------------------------用例直接调用处----------------------------

    def get_success_execute(self):
        text_center = self.success_execute()
        excel_center = StringCutting.specified_cut(self.overall[self.bi.whole_including()])
        print(text_center)
        print(excel_center)
        assert self.verify_dataframe(
            text_center, excel_center), \
            'Thead title display is incorrectly displayed.'
        pass

    def get_execute(self):

        info_text = self._visible_css_selectop_text(self.financial[self.bi.yaml_info()])
        pages = str.split(info_text, '，')[-1]

        pages = int(StringCutting.re_zip_code(pages, r'[1-9]\d'))
        if (pages % 10) > 0:
            number = 1
        else:
            number = 0
        pages = int((pages / 10)) + number
        self.log.info('There is data that needs to be paged: %s' % pages)

        self.tbody_list = []
        self.threads = []
        thead_tr = self.success_execute()

        queue = [i for i in range(1, pages + 1)]  # 构造 url 链接 页码。
        current = self.driver.current_url
        for qe in queue:
            url = current + '?page={}'.format(qe)
            thread = threading.Thread(target=self.success_tbody, args=(url, thead_tr,))
            thread.setDaemon(True)
            thread.start()
            self.threads.append(thread)
            time.sleep(1)

        for th in self.threads:
            th.join()

        self.log.log_ppriny(self.tbody_list[0])
