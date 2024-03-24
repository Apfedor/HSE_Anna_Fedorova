# Напишите функцию для валидации ИНН (идентификационного номера
# налогоплательщика), которая принимает в качестве аргумента строку, содержащую
# ИНН или просто набор цифр, похожий на ИНН.
def INN_is_valid(f: tuple):
    v1 = (2, 4, 10, 3, 5, 9, 4, 6, 8, 0)
    v2 = (7, 2, 4, 10, 3, 5, 9, 4, 6, 8)
    v3 = (3, 7, 2, 4, 10, 3, 5, 9, 4, 6, 8)
    promt1 = 'ИНН прошло валидацию'
    promt2 = 'ИНН не прошло валидацию'
    if len(f) == 10:
        valid = promt1 if ConNum(f, v1) == f[9] else promt2
    else:
        valid = promt1 if ConNum(f, v2) == f[10] and ConNum(f, v3) == f[11] else promt2
    return valid


def ConNum(v1: tuple, v2: tuple):
    con_sum = 0
    for i in range(len(v2)):
        con_sum += v1[i] * v2[i]
    con_mod = con_sum % 11
    return con_mod % 10 if con_mod > 9 else con_mod


def INN_valid():
    try:
        f = tuple(int(i) for i in tuple(input('Введите ИНН: ')))
        print(INN_is_valid(f) if len(f) == 10 or len(f) == 12 else 'Введено некорректное ИНН')
    except ValueError:
        print('Введены некорректные данные')
    pass


INN_valid()
