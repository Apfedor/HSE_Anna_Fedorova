#Домашнее задание 1
#Задание 1
#Поработайте с переменными, создайте несколько, выведите на экран.
# Запросите у пользователя некоторые числа и строки и сохраните в переменные, а затем выведите на экран.
# Используйте функции для консольного ввода input() и консольного вывода print().
#Попробуйте также через встроенную функцию id() понаблюдать, какие типы объектов могут изменяться и
# сохранять за собой адрес в оперативной памяти.

def example1():
    promt1 = 'Пример сложения:'
    promt2 = 'Вы ввели следующую строку:'

    b1 = input('Введите целое число x1: ')
    b2 = input('Введите целое число x2: ')

    if b1.isdigit() and b2.isdigit():
        d = [45, 123.2, 'привет', b1]
        d = int(d[3])
        d = d + int(b2)
    else:
        print('Некорректный ввод данных')
        exit()

    c=input('Введите строку: ')

    print(promt1, 'x1 + x2 =', b1, '+', b2, '=', d)
    print(promt2, c)

    print(id(b1))

    pass


example1()

