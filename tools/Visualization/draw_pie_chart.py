# -*- coding: utf-8 -*-

# @author:  dingdong
# @license: (C) Copyright 2016-2019, Ding dong online.
# @software: PyCharm
# @file:  draw_pie_chart.py
# @time: 2019/8/20 14:44
# @Software: PyCharm
# @Site    : 
# @desc:   绘制饼状图

import random

import matplotlib.pyplot as plt

from tools.hex_color import HexColor


class DrawPieChart(object):

    def __init__(self, source: dict, title: str = "各数据之间的占比为"):
        """
        准备数据
        """
        self.title = title

        self.calculate_proportion(source)
        pass

    def calculate_proportion(self, source):
        self.proportion = []
        self.data_title = source.keys()
        self.total = sum([int(i) for i in source.values()])

        for proportion in source.values():
            self.proportion.append(int(proportion) / self.total * 100)
        pass

    def get_show_color(self):
        """
        根据数据项的长度来设置颜色
        :return:
        """
        colors = []
        random_lis = []

        # 过滤一些从父类哪里继承过来的参数
        for i in dir(HexColor):
            if "__" in i:
                pass
            else:
                colors.append(i)
            pass
        # 裁剪出自己需要的长度
        # 方式一:
        pro_len = len(self.proportion)
        while (len(random_lis) < pro_len):
            x = random.randint(0, len(colors)-1)
            if x not in random_lis:
                random_lis.append(colors[x])

        # 方式二:
        # colors = colors[:len(self.proportion)]

        colors = random_lis

        del pro_len
        del random_lis

        return colors

    def show_chart(self):

        # 用来正常显示中文标签
        # plt.rcParams['font.sans-serif'] = ['SimHei']

        # 用来正常显示负号
        plt.rcParams['axes.unicode_minus'] = False

        # 绘制的图片为正圆
        plt.figure(figsize=(5, 5))

        # 设定各项距离圆心n个半径
        radius = [0.01, 0.01, 0.01]

        # 各饼块的颜色
        colors = self.get_show_color()

        # 绘制饼图
        plt.pie(self.proportion, explode=radius, labels=self.data_title, colors=colors, autopct='%.2f%%')

        # 加入图例 loc =  'upper right' 位于右上角 bbox_to_anchor=[0.5, 0.5] # 外边距 上边 右边 borderaxespad = 0.3图例的内边距
        plt.legend(loc="upper right", fontsize=10, bbox_to_anchor=(1.1, 1.1), borderaxespad=0.3)

        # 绘制标题
        plt.title(self.title)

        # 删除一些不需要的数据,减少内存消耗;特别是list和dict数据
        del colors

        # 展示
        plt.show()


if __name__ == '__main__':
    total = {'男': 27, '女': "54", '其他': 77}
    draw_pie = DrawPieChart(total, "三个参数占比")
    draw_pie.show_chart()
