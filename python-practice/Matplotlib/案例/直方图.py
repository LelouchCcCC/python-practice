import random

from matplotlib import pyplot as plt

# 直方图绘制要进行分组，组数一般遵循下列公式：
# 组数 = 极差/组距  ---->   = (max(a) - min(a))/bin_width

a = [random.randint(70, 121) for i in range(100)]
d = 5  # 组距
num_bin = (max(a) - min(a)) // d  # 组数

plt.figure(figsize=(20, 8), dpi=80)
plt.hist(a,num_bin)
plt.xticks(range(min(a), max(a)+d, d))
plt.grid()
plt.show()
