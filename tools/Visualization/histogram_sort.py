# -*- coding: utf-8 -*-

# @author:  dingdong
# @license: (C) Copyright 2016-2019, Ding dong online.
# @software: PyCharm
# @file:  histogram_sort.py
# @time: 2019/8/22 16:34
# @Software: PyCharm
# @Site    : 
# @desc:

import matplotlib.pyplot as plt
import numpy as np

# 创建带数字标签的直方图
numbers = list(range(1, 11))

# np.array()将列表转换为存储单一数据类型的多维数组
# x = np.array(numbers)
x = ['北京', '天津', '上海', '杭州', '深圳', '广州', '香港', '武汉', '重庆', '成都', ]
y = np.array([a ** 2 for a in numbers])

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
colors = ['#00FFFF', '#7FFFD4', '#F08080', '#90EE90', '#AFEEEE',
          '#98FB98', '#B0E0E6', '#00FF7F', '#FFFF00', '#9ACD32']

plt.bar(x, y, width=0.5, align='center', color=colors)

plt.title('柱状图排序', fontsize=24)
plt.xlabel('坐标', fontsize=14)
plt.ylabel('数值', fontsize=14)

plt.xticks(x)  # 横坐轴标签
plt.yticks(y)  # 横坐轴标签

plt.tick_params(axis='both', labelsize=14)
plt.axis([0, 11, 0, 110])

for a, b in zip(x, y):
    plt.text(a, b + 1.2, '%.s' % b, ha='center', va='bottom', fontsize=7)

plt.show()
