from matplotlib import pyplot as plt
import random
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
y_3 = [random.randint(20, 35) for i in range(31)]
y_10 = [random.randint(20, 35) for i in range(31)]

x_3 = range(31)
x_10 = range(40, 71)
plt.figure(figsize=(20, 8), dpi=80)
plt.scatter(x_3, y_3, label='3月份')
plt.scatter(x_10, y_10, label='10月份')
# x_3 = x_3[::5]
# x_10 = x_10[::5]
x_label = ['3月{}日'.format(i+1) for i in x_3]
x_label += ['10月{}日'.format(i-39) for i in x_10]
x = list(x_3) + list(x_10)
plt.xticks(x[::3], x_label[::3], rotation=45)
plt.legend(loc='upper right')
plt.show()
