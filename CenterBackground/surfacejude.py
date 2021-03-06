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
from CenterBackground.customTabs import CustomTabs

from CenterBackground.judeVerification import JudgmentVerification


class SurfaceJude(JudgmentVerification):
    '''
    页面数据以及页面标题获取并判断
    '''

    def __init__(self, config, basename, centerName):
        '''
        定义模块数据信息
        :param module:   元素模块
        :param sheet:   用例标签名
        :param basename:  执行程序的文件名
        :param centerName:  元素所在的类
        '''
        JudgmentVerification.__init__(self, config, basename)
        self.bi = centerName()
        pass

    def designated_box(self, keys, box: str):
        """
        进入指定的tab或者城市
        :return:
        """
        # 根据类型读取相应的数据信息
        self.ct = CustomTabs(self.driver, self.financial[keys])
        self.ct.into_the_city(self.vac, box)
        pass

    def bs4_soup(self):
        label_text = self.driver.page_source
        soup = BeautifulSoup(label_text, "lxml")
        return soup

    def info_number(self):
        # 读取info的数据并把int数据切割
        info_text = self.bi.yaml_info()
        if info_text in self.financial:
            info_text = self._visible_css_selectop_text(self.financial[info_text])
            if info_text:
                pages = str.split(info_text, '，')[-1]

                pages = int(StringCutting.re_zip_code(pages, "\d+"))
                if (pages % 10) > 0:
                    number = 1
                else:
                    number = 0
                pages = int((pages / 10)) + number
                return pages
            else:
                return info_text
        else:
            self.log.debug("页面没有翻页按钮.")
            return False

    def traverseYield(self, thead_tr, tbody_class):
        '''
        :param thead_tr:  页面内容标题
        :param tbody_class:  页面内容展示项
        :return:
        '''
        _button = "button"
        thead_length = len(thead_tr)  # 判断一共会出现td的长度
        for tr in tbody_class:  # 遍历获取不同的tr
            tbody_tr = {}
            tr_td = tr.find_all('td')
            for tr_len in range(thead_length):  # 遍历读取tr中不同的td
                # 最好一个td时,应查询td下面的button数据并读取相应的数据信息
                if tr_len == thead_length - 1:
                    td_text = [td.text.replace(" ", "").replace("\n", "") for td in tr_td[tr_len].find_all(_button)]
                else:
                    td_text = tr_td[tr_len].text.replace(" ", "").replace("\n", "")
                tbody_tr[thead_tr[tr_len]] = td_text
            yield tbody_tr
        pass

    def success_execute(self):
        """
        获取thead标签中的元素text
        :return:
        """
        try:
            soup = self.bs4_soup()
            thead_th = soup.find('thead').find('tr').find_all('th')
            text_center = [str.strip(th.text).replace("\n", "") for th in thead_th]
            return text_center
        except AttributeError:
            self.log.error("success_execute--页面没有数据信息出现错误:AttributeError: 'find'")
            assert False
        except Exception as e:
            self.log.error("出现未知的错误 %s" % e)

    def success_tbody(self, url, thead_tr):
        try:
            self.driver.get(url)
            soup = self.bs4_soup()
            tbody_class = soup.find('tbody').find_all('tr')
            tr_yield = self.traverseYield(thead_tr, tbody_class)
            for text in tr_yield:
                self.tbody_list.append(text)
            pass
        except AttributeError:
            self.log.error("tbody布局中只有一个tr所以在find_all('tr'),的时候出现错误."
                           "AttributeError: 'NoneType' object has no attribute 'find_all'")

    def title_execute(self):
        '''
        获取页面标题
        :return:
        '''
        text_center = self.success_execute()
        excel_center = str.split(self.overall[self.bi.whole_including()], ',')
        self.debugging_log(text_center, excel_center, 'Thead title display is incorrectly displayed.')
        del text_center
        del excel_center
        pass

    def surface_execute(self):
        """
        1.根据分页信息判断需要获取数据的页面数量
        2.通过线程来执行获取任务
        :return:
        """
        # 1.根据info获取当前分页的总数
        pages = self.info_number()  # 获取into的总数据信息
        self.tbody_list = []
        self.threads = []

        queue = [i for i in range(1, pages + 1)]  # 构造 url 链接 页码。

        # 2.获取页面内容的key
        thead_tr = self.success_execute()

        # 3.通过线程来获取内容
        current = self.driver.current_url

        if pages:
            self.log.info("页面有翻页按钮")
            # 如果界面只有一行数据的话,执行下面遍历操作就会出现IndexError: list index out of range
            for qe in range(1, 3):
                url = current + '&page={}'.format(qe)
                thread = threading.Thread(target=self.success_tbody, args=(url, thead_tr,))
                thread.setDaemon(True)
                thread.start()
                self.threads.append(thread)
                time.sleep(1)

            for th in self.threads:
                th.join()

            pass
        else:
            self.log.error("页面没有翻页按钮")

            url = current + '&page={}'.format(1)
            thread = threading.Thread(target=self.success_tbody, args=(url, thead_tr,))
            thread.setDaemon(True)
            thread.start()
            self.threads.append(thread)
            time.sleep(1)

        # 判断页面是否出现报错的文字提示
        soup = self.bs4_soup()
        fatal_error = soup.br
        if fatal_error:
            fatal_error_pare = fatal_error.parent
            for i, child in enumerate(fatal_error_pare.children, start=1):
                if not child.name in ('div', 'table'):
                    self.log.error(child)
            assert False, "页面报错"
        pass

    def debugging_log(self, ct_default, ov_default, mesg):
        assert operator.eq(ct_default, ov_default), mesg
        pass
