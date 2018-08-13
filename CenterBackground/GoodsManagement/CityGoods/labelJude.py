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
@file: labelJude.py
@time: 2018/8/10 18:06
@desc:
'''
import time
import operator
import threading
from bs4 import BeautifulSoup
from tools import StringCutting
from CenterBackground.GoodsManagement import CityGoods
from CenterBackground.judgmentVerification import JudgmentVerification
from tools.excelname.adminGongsMana import CityGoodsPage


class LabelJude(JudgmentVerification):

    def __init__(self, option):
        JudgmentVerification.config_dist = CityGoods.add_key(option)
        JudgmentVerification.__init__(self)
        self.cGoods = CityGoodsPage()
        pass

    def bs4_soup(self):
        label_text = self.driver.page_source
        soup = BeautifulSoup(label_text, "html.parser")
        return soup

    def success_execute(self):
        soup = self.bs4_soup()
        thead_th = soup.find('tr', class_='success').find_all('th')
        thead_tr = []
        for th in thead_th:
            text = str.strip(th.text)
            thead_tr.append(text)
        return thead_tr

    def success_tbody(self, url):
        print("----------", url)
        self.driver.get(url)
        soup = self.bs4_soup()
        thead_tr = self.success_execute()
        tbody_class = soup.find('tbody').find_all('tr')
        tr_yield = self.traverseYield(thead_tr, tbody_class)
        for text in tr_yield:
            self.tbody_list.append(text)

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
                    td_text = ' '.join([str.strip(a_text.text) for a_text in tr_td[tr_len].find_all('button')])
                else:
                    td_text = str.strip(tr_td[tr_len].text)
                tbody_tr[thead_tr[tr_len]] = td_text
            yield tbody_tr

    def get_table_hover(self):
        soup = self.bs4_soup()
        thead_tr = soup.find('thead').find('tr', class_='active')
        text_center = thead_tr.find_all('th', class_='text-center')
        text_center = [text.text for text in text_center]
        text_center = ','.join(text_center)
        excel_center = self.overall[self.cGoods.whole_including()]
        assert operator.eq(text_center, excel_center), 'Thead title display is incorrectly displayed.'
        pass

    def get_execute(self):

        info_text = self._visible_css_selectop_text(self.financial[self.cGoods.yaml_info()])
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
        queue = [i for i in range(1, pages)]  # 构造 url 链接 页码。
        current = self.driver.current_url
        for qe in queue:
            url = current + '?page={}'.format(qe)
            thread = threading.Thread(target=self.success_tbody, args=(url,))
            thread.setDaemon(True)
            thread.start()
            self.threads.append(thread)
            time.sleep(1)

        for th in self.threads:
            th.join()

        import pprint
        print(len(tbody_list))
        pprint.pprint(tbody_list)
