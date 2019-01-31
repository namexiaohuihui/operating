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
@time: 2018/8/15 10:17
@desc:
'''
import time
import threading
from bs4 import BeautifulSoup
from CenterBackground.judeVerification import JudgmentVerification


class LabelJude(JudgmentVerification):

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
        soup = BeautifulSoup(label_text, "html.parser")
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
                if tr_len == 0:
                    td_text = tr_td[tr_len].text.replace("\n", "").replace(" ", "")
                else:
                    td_text = str.strip(tr_td[tr_len].text)
                tbody_tr[thead_tr[tr_len]] = td_text
            yield tbody_tr

    def success_execute(self):
        soup = self.bs4_soup()
        text_center = soup.find('thead').find('tr').find_all('th')
        text_center = [str.strip(th.text) for th in text_center]
        return text_center

    def success_tbody(self, thead_tr):
        soup = self.bs4_soup()
        tbody_class = soup.find('tbody').find_all('tr')
        tr_yield = self.traverseYield(thead_tr, tbody_class)
        for text in tr_yield:
            self.tbody_list.append(text)

    # --------------------------------------------------------
    # ---------------------用例直接调用进行使用-------------------
    # ---------------------success用例位置---------------------
    # --------------------------------------------------------

    def get_success_execute(self):
        text_center = self.success_execute()
        text_center = ','.join(text_center)
        excel_center = self.overall[self.bi.whole_including()]
        assert self.verify_dataframe(text_center, excel_center), 'Page title is not displayed correctly.'
        pass

    # --------------------------------------------------------
    # ---------------------用例直接调用进行使用-------------------
    # ---------------------days用例位置---------------------
    # --------------------------------------------------------
    def get_execute(self):
        # 存储页面数据信息
        self.tbody_list = []
        # 存储定时器状态
        threads = []
        # 获取标题元素
        thead_tr = self.success_execute()
        # 界面滑动到底部
        # self.vac.scrollBar_buttom(self.driver)
        for page in range(2):
            throughs = self._visible_returns_selectop(self.financial[self.bi.yaml_through()])
            last = len(throughs) - 1
            thread = threading.Thread(target=self.success_tbody, args=(thead_tr,))
            thread.setDaemon(True)
            thread.start()
            threads.append(thread)
            time.sleep(1)

            # 如果最后一个按钮为下一页，那么就进行获取数据并点击
            if self.bi.ele_next() in throughs[last].get_attribute(self.bi.ele_class()):
                pass
            else:
                break
            # 判断线程是否工作完毕
            for thread in threads:
                if not thread.is_alive():
                    threads.remove(thread)

            # 点击翻页按钮
            self.vac.element_click(throughs[last].find_element_by_tag_name('a'))

        for th in threads:
            th.join()

        # 打印获取到的内容
        self.log.log_ppriny(self.tbody_list)
        df = self.list_to_pandas(self.tbody_list, thead_tr, '订单编号')
        df.to_csv("foo.csv", index=False, encoding="gbk")

    def get_seven_days(self):
        locator = self.financial[self.bi.yaml_timename()]
        self.vac.css_click(self.driver, locator)
        locator = self.financial[self.bi.yaml_ranges()]
        ele = self.vac.is_visibles_css_selectop(self.driver, locator)
        for e in range(len(ele)):
            if ele[e].text == self.overall[self.bi.excle_time_zone()]:
                self.vac.element_click(ele[e])
                break
        # 点击搜索按钮
        from CenterBackground.GoodsManagement.Evaluation.groupJude import GroupJude
        self.vac.element_click(GroupJude.button_formSub(self, self.bi.yaml_search()))
        tbodyT = self.driver.find_element_by_tag_name('tbody').text.strip()
        if tbodyT:
            self.get_execute()
        else:
            self.log.log_ppriny('Data information cannot be searched under this condition')
        # 缺失跟mysql的数据信息比对
        pass
