При программировании на Python мы можем столкнуться с двумя типами ошибок:

Синтаксические ошибки — они появляются из-за нарушения синтаксиса языка, когда вы пишете исходный код.
Ошибки выполнения — появляются в уже скомпилированной программе в процессе ее выполнения. Подобные ошибки называются исключениями.
Например, если файл был удален, пока программа работала, попытка чтения несуществующего файла приведет к выбрасыванию исключений. Python не знает, что делать, и сообщает об ошибке.
# Блоки try/except
### task_1
Спровоцировать и обработать исключения разных типов:
NameError
ZeroDivisionError
FileExistsError

# Блоки finally и else
Блок try поддерживает необязательные блоки:

Блок else— срабатывает при штатном выполнении кода внутри блока try, то есть когда 
не произошло никаких ошибок.
Блок finally — наоборот, выполняется всегда после блока try вне зависимости от того, 
произошла ошибка или нет.

### task_2
Принять на вход от пользователя два числа a и b. Разделить a на b. Убедиться, что 
пользователь ввел числа и эти числа целые. Число b должно быть отличным от нуля.
Флоу решения:
Получить данные от пользователя.
Обработать исключение ошибки ввода.
Обработать исключение деления на 0.
Добавить блоки else и finally для вывода сообщений.

# Traceback (трассировка, трэйс) — 
отчет, который показывает стек вызовов, где появилась ошибка. Каждое исключение содержит краткую
информацию и полный путь до места ошибки.
Стек — тип данных, представляющий собой список элементов, организованных по принципу 
LIFO (англ. last in — first out, «последним пришел — первым вышел»). То есть добавление новых элементов 
и удаление существующих производится с одного конца, называемого вершиной стека. Первым из стека 
удаляется элемент, который был помещен туда последним.

### task_3
Написать класс с тремя методами, в одном из которых возникает исключение.
Сделать обработку исключения на разных уровнях.

# В Python мы можем принудительно вызвать исключение с помощью специальной инструкции raise

### task_4
Для магического метода __add__ класса Employee добавить обработку исключений при 
передаче в метод значений, которые должны быть объектами этого же класса или числом.
Написать тесты на обработку исключений.
