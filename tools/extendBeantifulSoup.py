# -*- coding: utf-8 -*-
__author__ = 'DingDong'
"""
@file: demob.py
@time: 2018/4/11 9:20
"""

import pandas as pd
from bs4 import BeautifulSoup

from utils.browser_establish import browser_confirm

"""
通过路径来获取旗下子标签的数据信息
"""


class ExtendBeantifulSoup():
    """
    通过该函数，可以指定一个位置以及旗下的元素标签。然后自动获取相应的数据信息
    """
    LABLE_ONE_TR = "tr"  # 该数据下的标签分级，这里是第一级
    LABLE_TWO_TD = "td"  # 该数据下的标签分级，这里是第二级

    def __init__(self, drivers, lablePath, daily=None):
        """
        初始化参数
        :param drivers:  浏览器对象
        :param lablePath:  需要获取数据的位置
        :param daily:  键值关系中的键
        """
        self.drivers = drivers
        self.lablePath = lablePath
        self.daily = daily
        # 定义数据容器
        self.dataSet = []

    def setLablePath(self, lable):
        # 设置元素路径
        self.lablePath = lable

    def getLableOneTr(self):
        # 获得一级元素标签
        return self.LABLE_ONE_TR

    def setLableOneTr(self, one):
        # 设置一级元素标签
        self.LABLE_ONE_TR = one

    def getLableTwoTd(self):
        # 获得二级元素标签
        return self.LABLE_TWO_TD

    def setLableTwoTd(self, two):
        # 设置二级元素标签
        self.LABLE_TWO_TD = two

    lable_one = property(getLableOneTr, setLableOneTr, doc="Element 1 was incorrectly labeled")
    lable_two = property(getLableTwoTd, setLableTwoTd, doc="Element 2 was incorrectly labeled")

    def getDataSet(self):
        # 返回数据
        return self.dataSet

    def getDataRow(self):
        # 获取数据行数
        if self.dataSet:
            return len(self.dataSet)
        else:
            return 0

    def getDataColumn(self):
        # 获取数据列数
        if self.dataSet:
            return len(self.dataSet[0])
        else:
            return 0

    def lxml_to_beautiful(self, datatleThead):
        # 将数据进行转换成BeautifulSoup
        self.soup = BeautifulSoup(datatleThead, "lxml")

    def htmlToSoup(self):
        '''
        获取网页数据并将其转成BeautifulSoup
        :return:
        '''
        # 获取页面数据
        datatleThead = self.drivers.page_source

        # 将数据进行转换成BeautifulSoup
        self.lxml_to_beautiful(datatleThead)

    def lable_table_parsing(self, table):
        self.htmlToSoup()
        adress = self.soup.select(self.lablePath)
        lableOne = adress[0].find(table)
        lableOne = lableOne.find_all(self.lable_one)
        return lableOne

    def lableParsing(self):
        self.htmlToSoup()

        # 查找：在BeautifulSoup中是否有下面路径的数据
        adress = self.soup.select(self.lablePath)
        # 查找路径下面全部关于此标签的内容
        lableOne = adress[0].find_all(self.lable_one)
        return lableOne

    def lableParsingKey(self):
        """
        :return:  返回单次获取到的数据，并以key-value关系返回
        """
        lableOne = self.lableParsing()
        print(lableOne)
        for one in lableOne:  # 循环
            daily = {}  # 查找的内容通过键值关系进行输出
            # 查找路径下面全部关于此标签的内容
            lableTwo = one.find_all(self.lable_two)
            for two in range(len(lableTwo)):
                lable = lableTwo[two]  # 根据two位置来获取lableTwo中的数据
                # 将数据通过key-value关系保存
                daily[self.daily[two]] = lable.text.strip()
            # 添加到数据容器中
            self.dataSet.append(daily)
            return self

    def lable_cutting_tags(self, cutting, tags):
        self.lable_two = tags
        for lable in cutting:  # 循环
            # 查找路径下面全部关于此标签的内容
            lableTwo = lable.find_all(self.lable_two)
            # 将数据转换成列表形式进行输出
            daily = map(lambda lable: lable.text.replace('\n', '').strip(), lableTwo)
            # daily = map(lambda lable: lable.text.replace('\n', '|').replace(' ', '').strip(), lableTwo)
            self.dataSet.append(daily)

    def lable_table_list(self, table, th="th"):
        # 查找：在BeautifulSoup中是否有下面路径的数据
        # 查找路径下面全部关于此标签的内容
        lableOne = self.lable_table_parsing(table)
        self.lable_cutting_tags(lableOne, th)
        return self

    def lableParsingList(self, td="td"):
        """
        :return: 返回单次获取到的数据，并以list形式返回
        """
        lableOne = self.lableParsing()
        self.lable_cutting_tags(lableOne, td)
        return self

    def lable_parsing_cssselector(self, parsing, span=None):
        self.htmlToSoup()
        import time
        # 查找：在BeautifulSoup中是否有下面路径的数据
        adress = self.soup.select(self.lablePath)
        print("-----------------")
        print(adress)
        time.sleep(1)
        lableOne = adress[0].find_all(parsing)
        print("-----------------")
        print(lableOne)
        time.sleep(1)
        span = lableOne.find(span)
        print("-----------------")
        print(span.text)
        time.sleep(1)
        # daily = map(lambda one: one.text.strip(), lableOne)

    def interfaceToPandas(self):
        # 将数据转换成pandsa
        if self.dataSet:
            df = pd.DataFrame(self.dataSet, index=range(len(self.dataSet)), columns=self.daily)
            return df
        else:
            return 0


def fangshiyi():
    be = browser_confirm()
    drivers = be.url_opens(r"F:\desktop\buzhidao.html")
    ebs = ExtendBeantifulSoup(drivers, ".table.table-striped>thead")
    # ebs = ExtendBeantifulSoup(drivers, "#datatatle > thead")
    ebs.htmlToSoup()
    print(len(ebs.soup.find("tr")))
    for th in ebs.soup.find("tr"):
        if th.string.strip():
            print(th.string.strip())
    drivers.close()


if __name__ == '__main__':
    be = browser_confirm()
    drivers = be.url_opens(r"F:\desktop\buzhidao.html")
    ebs = ExtendBeantifulSoup(drivers, ".table.table-striped")
    # ebs = ExtendBeantifulSoup(drivers, "#datatatle > thead")
    # for dada in ebs.lable_table_list('thead', 'th').dataSet:
    #     print(list(dada))
    print(ebs.lable_table_list('tbody', 'td').interfaceToPandas())
    drivers.close()
