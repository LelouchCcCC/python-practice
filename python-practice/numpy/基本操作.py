import numpy as np

a = np.array([1, 2, 3, ])
# print(a)
# print(type(a))

t3 = np.arange(3, 10.1, 1)
print(t3)
print(t3.astype(int))
print(t3.astype(float))
print(t3.view())

a = np.array(range(0, 10), dtype=float)
print(a)
print('*' * 100)

t1 = np.arange(20).reshape(5, 4)
print(t1)
print(t1 * 2)
print('*' * 100)
arr = np.arange(0, 20).reshape(4, 5)
print(arr < 10)
print(arr[arr<10])
