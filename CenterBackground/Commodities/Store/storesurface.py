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
@file:      StoreSurface.py
@time:      2018/8/30 15:40
@desc:
'''
import time
import threading
from tools import StringCutting
from CenterBackground.Commodities.surfacejude import SurfaceJude


class StoreSurface(SurfaceJude):
    def __init__(self, module, sheet, basename, centerName):
        '''
        定义模块数据信息
        :param module:   元素模块
        :param sheet:   用例标签名
        :param basename:  执行程序的文件名
        :param centerName:  元素所在的类
        '''
        SurfaceJude.__init__(self, module, sheet, basename, centerName)
        pass

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
                if tr_len == 0:
                    tr_th = tr.find('th')
                    td_text = tr_th.input['value']
                else:
                    tr_td = tr.find_all('td')
                    td_text = str.strip(tr_td[tr_len - 1].text)
                tbody_tr[thead_tr[tr_len]] = td_text
            yield tbody_tr

    def success_tbody(self, url, thead_tr):
        self.driver.get(url)
        soup = self.bs4_soup()
        tbody_class = soup.find('tbody').find_all('tr')
        tr_yield = self.traverseYield(thead_tr, tbody_class)
        for text in tr_yield:
            self.tbody_list.append(text)

    def surface_execute(self):
        self.vai.scrollBar_buttom(self.driver)  # 界面滑动到浏览器底部
        pages = self.info_number()  # 获取into的总数据信息
        self.log.info('There is data that needs to be paged: %s' % pages)

        self.tbody_list = []
        self.threads = []
        thead_tr = self.success_execute()

        queue = [i for i in range(1, pages + 1)]  # 构造 url 链接 页码。
        current = self.driver.current_url
        for qe in range(1, 2):
            url = current + '?page={}'.format(qe)
            thread = threading.Thread(target=self.success_tbody, args=(url, thead_tr,))
            thread.setDaemon(True)
            thread.start()
            self.threads.append(thread)
            time.sleep(1)

        for th in self.threads:
            th.join()
        pass
