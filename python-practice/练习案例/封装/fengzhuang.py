class Phone:
    __is_5g_enable = None

    def __init__(self, ena):
        self.__is_5g_enable = ena

    def __check_5g(self):
        if self.__is_5g_enable:
            print('5g开启')
            return True
        else:
            print('5g关闭')
            return False

    def call_by_5g(self):
        if self.__check_5g():
            print('正在通话中')

p = Phone(True)
p.call_by_5g()