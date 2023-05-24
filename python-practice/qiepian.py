str = 'ejfi，黑马程序员，mcido'
num1 = str.index('黑')
num2 = str.index('员')
print(num1,num2)
pp = str[num2:num1-1:-1]
print(pp)