
# dop zadacha
# на входе от пользователя будет строка в виде арифметического выражения любой длины, записанного по законам математики.
# Например, 3 + 3 * 4 - 6 / 2
# надо посчитать результат через рекурсию
# ответ будет 12




# Задача 1: Напишите программу, которая на вход принимает
# два числа A и B, и возводит число А в целую степень B с
# помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8
"""
def power(A, B):
    # Базовый случай
    if B == 0:
        return 1
    # Рекурсивный случай
    return A * power(A, B - 1)

# Примеры использования
A1, B1 = 3, 5
print(f'{A1} ^ {B1} = {power(A1, B1)}')

A2, B2 = 2, 3
print(f'{A2} ^ {B2} = {power(A2, B2)}')

"""

# Задача 2: Напишите рекурсивную функцию sum(a, b),
# возвращающую сумму двух целых неотрицательных чисел. Из
# всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы.

# 2 2
# 4
"""
def sum(a, b):
    # Базовый случай: если одно из чисел равно 0
    if a == 0:
        return b
    if b == 0:
        return a
    
    # Рекурсивный случай: уменьшаем a и увеличиваем b
    return sum(a - 1, b + 1)

# Примеры использования
a1, b1 = 2, 2
print(f'Sum of {a1} and {b1} = {sum(a1, b1)}')
"""

# arr = [18, [[20,[10,7]],15]]

"""
PRACTICHESKA ROBOTA 1 DZ

# Функция для поиска ключа в словаре или списке с учётом глубины поиска
def find_key(struct, key, max_depth=None, depth=1):
    result = None  # Переменная для хранения найденного значения
    
    # Если указана максимальная глубина и текущая глубина превышает её, прекращаем поиск
    if max_depth and max_depth < depth:
        return result
    
    # Если ключ найден в текущем уровне словаря, возвращаем его значение
    if isinstance(struct, dict):
        if key in struct:
            return struct[key]
        # Рекурсивный поиск по вложенным словарям
        for sub_struct in struct.values():
            result = find_key(sub_struct, key, max_depth, depth=depth + 1)
            if result:
                break

    # Если структура - это список
    elif isinstance(struct, list):
        for item in struct:
            result = find_key(item, key, max_depth, depth=depth + 1)
            if result:
                break

    return result

# Пример словаря и списка с вложенными структурами
site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
        }
    }
}

arr = [18, [[20, [10, 7]], 15]]

while True:
    key = input('Введите искомый ключ: ')  # Запрашиваем ключ у пользователя
    answer = input('Хотите ввести максимальную глубину? Y/N: ')  # Проверяем, хочет ли пользователь ограничить глубину поиска
    
    if answer.lower() == 'y':
        max_depth = int(input('Введите максимальную глубину: '))  # Если да, запрашиваем максимальную глубину
    else:
        max_depth = None  # Если нет, устанавливаем максимальную глубину как None
    
    # Выводим найденное значение ключа или None, если ключ не найден
    print('Значение ключа в словаре site:', find_key(struct=site, key=key, max_depth=max_depth))
    print('Значение ключа в списке arr:', find_key(struct=arr, key=key, max_depth=max_depth))

"""

# PRACTICHESKA ROBOTA 1 DZ
"""
import copy

# Исходная структура сайта
site = {
    'html': {
        'head': {
            'title': 'Куплю/продам телефон недорого'
        },
        'body': {
            'h2': 'У нас самая низкая цена на iPhone',
            'div': 'Купить',
            'p': 'Продать'
        }
    }
}

# Функция для замены значения в структуре словаря
def change_value(struct, key, value):
    if key in struct:
        struct[key] = value
    else:
        for sub_struct in struct.values():
            if isinstance(sub_struct, dict):
                change_value(sub_struct, key, value)
    return struct

# Функция для отображения структуры сайта
def display_struct(struct, spaces=1):
    for key, value in struct.items():
        if isinstance(value, dict):
            print(' ' * spaces, key)
            display_struct(value, spaces + 3)
        else:
            print("{}{} : {}".format(' ' * spaces, key, value))

# Функция для создания сайта под конкретный продукт
def make_site(name):
    struct_site = copy.deepcopy(site)  # Глубокое копирование исходного сайта
    new_title = 'Куплю/продам {} недорого'.format(name)  # Изменяем заголовок
    struct_site = change_value(struct_site, 'title', new_title)
    new_h2 = 'У нас самая низкая цена на {}'.format(name)  # Изменяем заголовок второго уровня
    struct_site = change_value(struct_site, 'h2', new_h2)
    return struct_site

# Основная часть программы
sites = []
sites_count = int(input('Сколько сайтов: '))
for _ in range(sites_count):
    product_name = input('Введите название продукта для нового сайта: ')
    new_site = make_site(product_name)
    sites.append(new_site)

for i_site in sites:
    display_struct(i_site)
""" 

# PRACTICKA 3 DZ
""" 
def my_sum(*args):
    total_sum = 0  # Инициализация переменной для хранения суммы
    for i_elem in args:
        # Проверка, является ли элемент целым числом
        if isinstance(i_elem, int):
            total_sum += i_elem  # Добавление числа к общей сумме
        # Проверка, является ли элемент списком или кортежем
        elif isinstance(i_elem, (list, tuple)):
            # Рекурсивный вызов функции для суммирования элементов внутри списка или кортежа
            for x in i_elem:
                total_sum += my_sum(x)
    return total_sum

# Основной код для тестирования
print(my_sum([[1, 2, [3]], [1], 3]))  # Ожидаемый результат: 10
# print(my_sum(1, 2, 3, 4, 5))  # Ожидаемый результат: 15
""" 

# PRACTICA 4 DZ


def flatten(a_list):
    # Инициализация пустого списка для хранения результата
    result = []
    # Перебор каждого элемента в списке
    for e in a_list:
        # Проверка, является ли элемент целым числом
        if isinstance(e, int):
            result.append(e)  # Добавление числа в результат
        else:
            # Рекурсивный вызов функции для вложенного списка
            result.extend(flatten(e))  # Раскрытие вложенных списков
    # Возвращаем окончательный результат
    return result

# Исходный список с вложенными элементами
nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]], [[11, 12, 13], [14, 15], [16, 17, 18]]]

# Применение функции для получения списка с раскрытыми элементами
flattened_list = flatten(nice_list)

# Вывод результата
print(flattened_list)  # Ожидаемый результат: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
