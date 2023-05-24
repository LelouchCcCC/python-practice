float_num = float(-11.864)
print(float_num)
int_num = int(float_num)
print(int_num)

a = '\'fmnfe\''
print(a)

name = 'zhangyu'
sex = 'male'
bb = 'name: %s, sex: %s' % (name, sex)
print(bb)

# 数字限制
print('------')
num1 = 11
num2 = 11.345
print('%5d' % num1)
print('%1d' % num1)
print('%7.2f' % num2)
print('%.2f' % num2)
print('------')

# 快速格式化
print(f"我{num1},;{num2}")