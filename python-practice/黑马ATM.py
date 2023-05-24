money = 5000000
name = None


def query(name):
    print(f'剩余的金额为{money}')
    return 0


def cun(name, num):
    global money
    money += num
    print(f'已经存好了')
    return 0


def qu(name, num):
    global money
    if money - num < 0:
        print('钱不够取')
    else:
        money -= num
        print('存好了')
    return 0


def main():
    return input()


while True:
    keyboard_input = main()
    if keyboard_input == '1':
        query(name)
    elif keyboard_input == '2':
        cun(name, 100)
    elif keyboard_input == '3':
        qu(name, 200)
    else:
        break
