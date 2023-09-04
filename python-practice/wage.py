import random

total = 10000
num = 20
for i in range(1, 21):
    fen = random.randint(0, 10)
    if fen < 5:
        print(f'员工{i}，绩效分{fen}，低于5，不发工资，下一位')
        continue
    elif total >= 1000:
        total -= 1000
        print(f'向员工{i}发放工资1000元，账户余额还剩余{total}元')
    else:
        print('工资发放完了，下个月再领取吧')
        break
