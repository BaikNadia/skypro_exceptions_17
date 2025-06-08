class MyClass:

    def func1(self):
        1 / 0
        print('Работает метод func1')

    def func2(self):
        self.func1()
        print('Работает метод func2')

    def func3(self):
        self.func2()
        print('Работает метод func3')


if __name__ == '__main__':                # без блока try/except появятся ошибки
    try:                                  # снизу вверх
        my_obj = MyClass()
        my_obj.func3()
    except ZeroDivisionError:
        print('На ноль делить нельзя')
