from random import randint

'''Сгенерируйте массив из целых чисел, содержащий 100 000 элементов, с помощью функции randomint из модуля random.'''


def random_list(length) -> list:
    return [randint(0, length) for _ in range(length)]


def task1():
    print(random_list(100_000))


'''Сгенерируйте с помощью функции range массив, содержащий словари со следующей структурой:
{
    “num_1”: randomint(1,1_000_000), 
    “num_2”: randomint(1,1_000_000)
}
Длина массива должна составлять 100 000 элементов.'''

def gen_Dict(length) -> list:
    return [{f'num_{i}': randint(1, 1_000_000) for i in range(1, 3)} for _ in range(length)]


def task2():
    # print(random_dict(100_000))
    print(gen_Dict(100))


'''Напишите функцию алгоритма сортировки пузырьком и с её помощью отсортируйте первый массив.'''


def bubble(array):
    iterations = len(array) - 1
    for i in range(iterations):
        for j in range(iterations - i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]


def task3():
    a = random_list(100)
    bubble(a)
    print(a)



'''Отсортируйте второй массив с помощью встроенного спиского метода .sort() и лямбда-функции сначала по первому ключу, потом по второму'''


def task4():
    a = random_list(100)
    print(a)
    a.sort()
    print(a)
    a = gen_Dict(100)
    a.sort(key=lambda x: x['num_1'])
    print(a)
    a = gen_Dict(100)
    a.sort(key=lambda x: x['num_2'])
    print(a)


task4()




