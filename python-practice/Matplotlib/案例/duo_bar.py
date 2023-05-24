from matplotlib import pyplot as plt

a = ['finals', 'spiderman', 'dunkerk', 'fighters']
b_16 = [1194, 342, 543, 324]
b_15 = [1694, 842, 243, 124]
b_14 = [194, 423, 1434, 507]

bar_width = 0.2

x_14 = list(range(len(a)))
x_15 = [i + bar_width * 1.1 for i in x_14]
x_16 = [i + bar_width * 2.2 for i in x_14]

plt.figure(figsize=(20, 8), dpi=80)

plt.bar(range(len(a)), b_14, width=bar_width)
plt.bar(x_15, b_15, width=bar_width)
plt.bar(x_16, b_16, width=bar_width)

plt.xticks(x_15, a)

plt.show()
