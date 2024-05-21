from datetime import datetime
from random import randint


def timer(func):
    def wrapper(**kwargs):
        start_time = datetime.now()
        result = func(**kwargs)
        end_time = datetime.now()
        duration = end_time - start_time
        print(f"\n{func.__name__} --- Выполнена за {duration} секунд")
        return result

    return wrapper


@timer
def binary_search(**kwargs) -> bool:
    low = 0
    high = len(kwargs['array']) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = kwargs['array'][mid]
        if guess < kwargs['item']:
            low = mid + 1
        elif guess > kwargs['item']:
            high = mid - 1
        else:
            return True
    return False


@timer
def linear_search(**kwargs):
    if kwargs['item'] in kwargs['array']:
        return True
    else:
        return False


def random_array(start: int, limit: int, step: int) -> list:
    return list(i for i in range(start, limit, step))


def task_1():
    start = 1
    limit = 100_000_000
    r_array = random_array(start=start, limit=limit, step=randint(3, 4))
    print(f"Длина массива - {len(r_array)}")
    n_1, n_2, n_3 = randint(start, limit), randint(start, limit), randint(start, limit)
    print(f'Число {n_1} в массиве - {linear_search(array=r_array, item=n_1)}')
    print(f'Число {n_2} в массиве - {linear_search(array=r_array, item=n_2)}')
    print(f'Число {n_3} в массиве - {linear_search(array=r_array, item=n_3)}')
    print(f'Число {n_1} в массиве - {binary_search(array=r_array, item=n_1)}')
    print(f'Число {n_2} в массиве - {binary_search(array=r_array, item=n_2)}')
    print(f'Число {n_3} в массиве - {binary_search(array=r_array, item=n_3)}')


task_1()
