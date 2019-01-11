# -*- coding: utf-8 -*-
"""
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
@file:      visual_induction.py
@time:      2019/1/9 10:44
@desc:
https://blog.csdn.net/qq_34859482/article/details/80617391
"""
import matplotlib.pyplot as plt
import numpy as np


class VisualInduction(object):
    def __init__(self):
        # self.color_argument()
        pass

    def single_figure(self):
        # 创建画板
        fig = plt.figure()

        # 在画板的第1行第1列的第一个位置生成一个Axes对象来准备作画
        # 也可以通过fig.add_subplot(2, 2, 1)的方式生成Axes
        ax = fig.add_subplot(111)

        # xlim横坐标的范围值,xlabel横坐标的单位
        # ylim纵坐标的范围值,ylabel纵坐标的单位
        ax.set(xlim=[0.5, 4.5], ylim=[-2, 8], title='An Example Axes',
               ylabel='Y-Axis', xlabel='X-Axis')
        pass

    def more_figure(self):
        fig, axes = plt.subplots(nrows=2, ncols=2)
        ax1 = axes[0, 0]
        ax2 = axes[0, 1]
        ax3 = axes[1, 0]
        ax4 = axes[1, 1]

        x = np.linspace(0, np.pi)
        y_sin = np.sin(x)
        y_cos = np.cos(x)

        # 前面两个参数为x轴、y轴数据。
        # ax2的第三个参数是 MATLAB风格的绘图，对应ax3上的颜色，marker为点显示的样式。
        ax1.plot(x, y_sin)
        ax2.plot(x, y_sin, 'go--', linewidth=2, markersize=12)
        ax3.plot(x, y_cos, color='red', marker='+', linestyle='dashed')

        ax1.set(xlim=[0.5, 4.5], ylim=[-2, 8], title='Upper Left', ylabel='Y-Axis', xlabel='X-Axis')

        ax2.set(xlim=[0.5, 4.5], title='Upper Right', ylabel='Y-Axis', xlabel='X-Axis')

        ax3.set(ylim=[-2, 8], title='Lower Left', ylabel='Y-Axis', xlabel='X-Axis')

        ax4.set(xlim=[0.5, 4.5], ylim=[-2, 8], title='Lower Right', )

    def color_argument(self):
        x = np.linspace(0, 20, 200)
        data_obj = {'x': x,
                    'y1': 2 * x + 1,
                    'y2': 3 * x + 1.2,
                    'mean': 0.5 * x * np.cos(2 * x) + 2.5 * x + 1.1}
        print(x)
        fig, ax = plt.subplots()

        # 填充两条线之间的颜色:第一个参数为横坐标的内容，第二和第三个参数为填充范围
        ax.fill_between('x', 'y1', 'y2', color='yellow', data=data_obj)

        # 设置线条的颜色:前面两个参数为x轴、y轴数据
        ax.plot('x', 'mean', color='black', data=data_obj)

    def draw_some(self):
        x = np.arange(10)
        print(x)
        y = np.random.randn(10)
        print(y)
        plt.scatter(x, y, color='red', marker='+')

    def draw_bar(self):
        """条形图分两种，一种是水平的，一种是垂直的"""
        np.random.seed(1)
        x = np.arange(5)
        y = np.random.randn(5)

        fig, axes = plt.subplots(ncols=2, figsize=plt.figaspect(1. / 2))

        # 条形的图的颜色color,条形图的样式
        vert_bars = axes[0].bar(x, y, color='lightblue', align='center')
        horiz_bars = axes[1].barh(x, y, color='yellow', align='edge')

        # 在水平或者垂直方向上画线,linewidth为轴的宽度,轴颜色color
        axes[0].axhline(0, color='gray', linewidth=2)
        axes[1].axvline(0, color='gray', linewidth=6)

        fig1, ax1 = plt.subplots()
        vert_bars = ax1.bar(x, y, color='lightblue', align='center')

        # We could have also done this with two separate calls to `ax.bar` and numpy boolean indexing.
        for bar, height in zip(vert_bars, y):
            if height < 0:
                bar.set(edgecolor='darkred', color='salmon', linewidth=3)

    def drow_histogram(self):
        np.random.seed(19680801)

        n_bins = 10
        x = np.random.randn(1000, 3)

        fig, axes = plt.subplots(nrows=2, ncols=2)
        ax0, ax1, ax2, ax3 = axes.flatten()

        colors = ['red', 'tan', 'lime']
        ax0.hist(x, n_bins, density=True, histtype='bar', color=colors, label=colors)
        # 图标颜色说明
        ax0.legend(prop={'size': 10})
        ax0.set_title('bars with legend')

        ax1.hist(x, n_bins, density=True, histtype='barstacked')
        ax1.set_title('stacked bar')

        ax2.hist(x, histtype='barstacked', rwidth=0.9)

        ax3.hist(x[:, 0], rwidth=0.9)
        ax3.set_title('different sample sizes')

        fig.tight_layout()

    def show_visual(self):
        # 显示画板
        plt.show()


if __name__ == '__main__':
    visual = VisualInduction()
    visual.drow_histogram()
    visual.show_visual()
