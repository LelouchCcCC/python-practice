str = '21fmeomom12 '
print(str.strip())
print(str.strip('21f6'))
print(str.strip().strip('21f6'))

set = {'fer':'fe'}
print(type(set))

set1 = {1,2,3}
set2 = {6,5,1}
print(set2.difference(set1))

def info(*args):
    for i in args:
        print(i, end=' ')
    return 0

def inin(**kwargs):
    for i in kwargs.keys():
        print(kwargs[i], end=' ')
    return 0

info('dwr',234,454,4654,'efr')
print()
inin(p=434,a=3435,o=3455,l=23423)


