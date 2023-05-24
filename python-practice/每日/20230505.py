import numpy as np
def ad(x, y):
    """
    通过此可以实现两数相除
    :param x: 除数
    :param y: 被除数
    :return: 返回其结果
    """
    return x / y


ad(5, 6)

num = 3


def a1():
    global num
    # num = 4
    print(f"num:{num}")


a1()

list = ['ekvr', 854, 'mendi', 854]
# print(list.index(8545))
list.extend([1, 4, 6])
print(f'追加后的结果为{list}')

list = ['ekvr', 854, 'mendi', 854]
del list[2]
print(list)
list = ['ekvr', 854, 'mendi', 854]
sc = list.pop(2)
print(f'删除的元素为{sc}，剩余列表结果为{list}')


x = np.array([[1,2,3],[4,5,6]])
print(x[0,:])
print(x[:,0])
print('---------')
a = np.arange(0,9)
print(a)
print(a[2:-1])
print(a[-2:])
print(a[:-2])
print('---------')
a = np.arange(0,9)
print(a[::2])
print(a[::-3])
print(type(a[::3]))
