# -*- coding: utf-8 -*-
__author__ = 'DingDong'
"""
@file: demob.py
@time: 2018/4/11 9:20
"""

from utils.browser_establish import browser_confirm
from bs4 import BeautifulSoup
import pandas as pd
import time


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

    def setLableOneTr(self, one):
        # 设置一级元素标签
        self.LABLE_ONE_TR = one

    def setLableTwoTd(self, two):
        # 设置二级元素标签
        self.LABLE_TWO_TD = two

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

    def htmlToSoup(self):
        # 获取页面数据
        datatleThead = self.drivers.page_source

        # 将数据进行转换成BeautifulSoup
        self.soup = BeautifulSoup(datatleThead, "lxml")

    def lableParsing(self):
        self.htmlToSoup()

        # 查找：在BeautifulSoup中是否有下面路径的数据
        adress = self.soup.select(self.lablePath)

        # 查找路径下面全部关于此标签的内容
        lableOne = adress[0].find_all(self.LABLE_ONE_TR)

        return lableOne

    def lableParsingKey(self):
        """
        :return:  返回单次获取到的数据，并以key-value关系返回
        """
        lableOne = self.lableParsing()
        for one in lableOne:  # 循环
            daily = {}  # 查找的内容通过键值关系进行输出
            # 查找路径下面全部关于此标签的内容
            lableTwo = one.find_all(self.LABLE_TWO_TD)
            for two in range(len(lableTwo)):
                lable = lableTwo[two]  # 根据two位置来获取lableTwo中的数据
                # 将数据通过key-value关系保存
                daily[self.daily[two]] = lable.text.strip()
            # 添加到数据容器中
            self.dataSet.append(daily)
        return daily

    def lableParsingList(self):
        """
        :return: 返回单次获取到的数据，并以list形式返回
        """
        lableOne = self.lableParsing()
        for one in lableOne:  # 循环
            # 查找路径下面全部关于此标签的内容
            lableTwo = one.find_all(self.LABLE_TWO_TD)
            daily = []  # 查找的内容通过键值关系进行输出
            for two in lableTwo:
                daily.append(two.text.strip())
            self.dataSet.append(daily)
        return daily

    def interfaceToPandas(self):
        # 将数据转换成pandsa
        if self.dataSet:
            df = pd.DataFrame(self.dataSet, index=range(len(self.dataSet)), columns=self.daily)
            return df
        else:
            return 0


if __name__ == '__main__':
    daily = ["type", "city", "title", "content", "time", "status", "default"]

    be = browser_confirm()
    drivers = be.url_opens(r"F:\desktop\gonggao.html")

    db = ExtendBeantifulSoup(drivers, "#datatatle > tbody", daily)
    db.lableParsingList()
    db.interfaceToPandas()
    print(df)
    drivers.close()

    print(df.index)  # 打印所有序列名
    print(df.columns)  # 打印标题
