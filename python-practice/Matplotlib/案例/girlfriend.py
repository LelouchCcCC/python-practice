# -*- coding: utf-8 -*-

import random
from matplotlib import pyplot as plt

a = [1, 0, 1, 1, 2, 4, 3, 2, 3, 4, 4, 5, 6, 5, 4, 3, 3, 1, 1, 1]
b = [1, 0, 3, 1, 2, 2, 3, 3, 2, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1]
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

x = range(11, 31)
_x = list(x)[::4]
plt.figure(figsize=(20, 8), dpi=80)
plt.plot(x, a, 'r:', label='自己')
plt.plot(x, b, 'b--',label='同桌')
xtick_label = ['{}岁'.format(i) for i in _x]
plt.xticks(_x, xtick_label, rotation=45)
plt.yticks([min(a), max(a)])
plt.legend(loc='upper left')
plt.grid(alpha=0.4)
plt.show()
