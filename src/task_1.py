try:
    print(a)
except NameError:
    print('Обращение к несуществующей переменной')

try:
    1 / 0
except ZeroDivisionError:
    print('Нельзя делить на ноль')

try:
    open('some_file')
except FileExistsError:
    print('Файл не существует')