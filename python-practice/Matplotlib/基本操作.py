from matplotlib import pyplot as plt

x = range(0, 10, 2)
y = [10, 12, 17, 35, 9]

# 设置图片大小
plt.figure(figsize=(20, 8), dpi=80)  # （宽，高），dot per inch

# 绘图
plt.plot(x, y)

# 设置x,y轴刻度
plt.xticks([i/2 for i in range(0, 20)])
plt.yticks(range(min(y),max(y)+1,3))

# 保存
plt.savefig('./first.svg')

# 绘制网格
plt.grid()


# 展示图形
plt.show()
