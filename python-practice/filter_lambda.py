import math
new_list = list(filter(lambda x:math.sqrt(x) % 1 == 0, range(0,101)))
print(new_list)