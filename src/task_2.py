try:
    a, b = input('Введите числа: ').split()
    a, b = int(a), int(b)
    result = a / b
except ValueError as e:
    print(e)
except ZeroDivisionError as e:
    print(e)
else:
    print(result)
finally:
    print('Операция завершена')
