# -*- coding: utf-8 -*-

# @author:  dingdong
# @license: (C) Copyright 2016-2019, Ding dong online.
# @software: PyCharm
# @file:  line_chart.py
# @time: 2019/8/22 17:34
# @Software: PyCharm
# @Site    : 
# @desc:

#模块pyplot包含很多生成图表的函数
import matplotlib.pyplot as plt
import numpy as np
input_values = [1,2,3,4,5,6]
squares = [1,4,9,16,25,36]
#plot()绘制折线图
plt.plot(input_values,squares,linewidth=5)
#np.array()将列表转换为存储单一数据类型的多维数组
x = np.array(input_values)
y = np.array(squares)
#annotate()给折线点设置坐标值
for a,b in zip(x,y):
    plt.annotate('(%s,%s)'%(a,b),xy=(a,b),xytext=(-20,10),
                 textcoords='offset points')
#设置标题
plt.title('折线图',fontsize=24)
plt.xlabel('城市',fontsize=14)
plt.ylabel('数量',fontsize=14)
#设置刻度的大小,both代表xy同时设置
plt.tick_params(axis='both',labelsize=14)
#show()打开matplotlib查看器，并显示绘制的图形
plt.show()