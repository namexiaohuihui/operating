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
@author:    ln_company
@license:   (C) Copyright 2016- 2018, Node Supply Chain Manager Corporation Limited.
@Software:  PyCharm
@file:      surfacejude.py
@time:      2018/8/28 18:09
@desc:
'''
import operator
import time
import threading
from bs4 import BeautifulSoup
from tools import StringCutting
from CenterBackground import Commodities

from CenterBackground.judeVerification import JudgmentVerification


class SurfaceJude(JudgmentVerification):
    '''
    页面数据以及页面标题获取并判断
    '''
    def __init__(self, module, sheet, basename, centerName):
        '''
        定义模块数据信息
        :param module:   元素模块
        :param sheet:   用例标签名
        :param basename:  执行程序的文件名
        :param centerName:  元素所在的类
        '''
        JudgmentVerification.__init__(self, Commodities.add_key(module, sheet), basename)
        self.bi = centerName()
        pass

    def bs4_soup(self):
        label_text = self.driver.page_source
        soup = BeautifulSoup(label_text, "html.parser")
        return soup

    def info_number(self):
        # 读取info的数据并把int数据切割
        info_text = self._visible_css_selectop_text(self.financial[self.bi.yaml_info()])
        pages = str.split(info_text, '，')[-1]

        pages = int(StringCutting.re_zip_code(pages, r'[1-9]\d'))
        if (pages % 10) > 0:
            number = 1
        else:
            number = 0
        pages = int((pages / 10)) + number
        return pages

    def traverseYield(self, thead_tr, tbody_class):
        '''

        :param thead_tr:  页面内容标题
        :param tbody_class:  页面内容展示项
        :return:
        '''
        for tr in tbody_class:
            tbody_tr = {}
            thead_length = len(thead_tr)
            for tr_len in range(thead_length):
                tr_td = tr.find_all('td')
                if tr_len == thead_length -1:
                    td_text = [td.text for td in tr_td[tr_len].find('button')]
                else:
                    td_text = str.strip(tr_td[tr_len].text)
                tbody_tr[thead_tr[tr_len]] = td_text
            yield tbody_tr
        pass

    def success_execute(self):
        soup = self.bs4_soup()
        thead_th = soup.find('thead').find('tr').find_all('th')
        text_center = [str.strip(th.text) for th in thead_th]
        return text_center

    def success_tbody(self, url, thead_tr):
        self.driver.get(url)
        soup = self.bs4_soup()
        tbody_class = soup.find('tbody').find_all('tr')
        tr_yield = self.traverseYield(thead_tr, tbody_class)
        for text in tr_yield:
            self.tbody_list.append(text)
        pass

    def title_execute(self):
        '''
        获取页面标题
        :return:
        '''
        text_center = self.success_execute()
        excel_center = StringCutting.specified_cut(self.overall[self.bi.whole_including()])
        self.debugging_log(text_center, excel_center, 'Thead title display is incorrectly displayed.')
        pass

    def surface_execute(self):
        pages = self.info_number()  # 获取into的总数据信息
        self.log.info('There is data that needs to be paged: %s' % pages)

        self.tbody_list = []
        self.threads = []
        thead_tr = self.success_execute()

        queue = [i for i in range(1, pages + 1)]  # 构造 url 链接 页码。
        current = self.driver.current_url
        for qe in range(1,3):
            url = current + '&page={}'.format(qe)
            thread = threading.Thread(target=self.success_tbody, args=(url, thead_tr,))
            thread.setDaemon(True)
            thread.start()
            self.threads.append(thread)
            time.sleep(1)

        for th in self.threads:
            th.join()

        pass

    def debugging_log(self, ct_default, ov_default, mesg):
        print("--------------------------------")
        print(ct_default, type(ct_default))
        print(ov_default, type(ov_default))
        print("--------------------------------")
        assert operator.eq(ct_default, ov_default), mesg
        pass