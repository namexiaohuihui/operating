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
@file:      plarformsurface.py
@time:      2018/8/30 15:40
@desc:
'''
import time
import threading
from tools import StringCutting
from CenterBackground.surfacejude import SurfaceJude


class PlarformSurface(SurfaceJude):
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
        watikiType = ''  # 记录第二项的内容
        bindingGoods = ''  # 记录第三项的内容
        sorting = ''  # 记录第十三项的内容
        for tr in tbody_class:
            tbody_tr = {}
            tr_td = tr.find_all('td')
            td_length = len(tr_td)
            thead_length = len(thead_tr)
            for tr_len in range(thead_length):
                if td_length == thead_length:
                    if tr_len == 1:
                        watikiType = str.strip(tr_td[tr_len].text)
                        td_text = watikiType
                    elif tr_len == 2:
                        bindingGoods = str.strip(tr_td[tr_len].text)
                        td_text = bindingGoods
                    elif tr_len == 12:
                        sorting = str.strip(tr_td[tr_len].text)
                        td_text = sorting
                    elif tr_len == thead_length - 1:  # 最后一个td要区分
                        td_text = ' '.join([str.strip(a_text.text) for a_text in tr_td[tr_len].find_all('button')])
                    else:
                        td_text = StringCutting.spaces_replace(tr_td[tr_len].text)
                elif (td_length + 3) == thead_length:
                    if tr_len == 1:
                        td_text = watikiType
                        tr_td.insert(tr_len, watikiType)
                    elif tr_len == 2:
                        td_text = bindingGoods
                        tr_td.insert(tr_len, bindingGoods)
                    elif tr_len == 12:
                        td_text = sorting
                        tr_td.insert(tr_len, sorting)
                    elif tr_len == thead_length - 1:  # 最后一个td要区分
                        td_text = ' '.join([str.strip(a_text.text) for a_text in tr_td[tr_len].find_all('button')])
                    else:
                        td_text = StringCutting.spaces_replace(tr_td[tr_len].text)
                else:
                    self.log.info('traverseYield ---  error --- SurfaceJude')
                    self.log.info('%s ---  %s --- %s' % (tr_len, td_length, thead_length))
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
