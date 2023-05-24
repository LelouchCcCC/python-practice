# -*- coding: utf-8 -*-

import random
from matplotlib import pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
a = [random.randint(20, 35) for i in range(120)]
plt.figure(figsize=(20, 8), dpi=80)
x = range(120)
plt.plot(x, a)
_x = list(x)[::10]
xtick_label = ['{}:{:0<2d}'.format(10 + i // 60, i % 60) for i in _x]
plt.xticks(_x, xtick_label, rotation=45)
plt.yticks([min(a), max(a) + 1])
plt.show()
