"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.

Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75
"""
# из собственной библиотеки подключаю функцию контроля ввода числа
# функцию использовал в предыдущих работах, не буду загромождать
from lib import input_nbr


def recursion(numb, start=1, total=1):
    """Рекурсивное решение функции"""
    # Базовый случай
    # Последний шаг рекурсии
    if numb == 1:
        print(total)
        return
    # Шаг рекурсии / рекурсивное условие
    # numb уменьшаем на единицу, следующий элемент ряда получаем делением на
    # -2, получаем промежуточную сумму элементов
    recursion(numb - 1, start / (-2), total + start / (-2))

# код основной программы из задания


# пользователь вводит число
INP = input_nbr(
    'int',
    '> Введите натуральное число, которое требуется перевернуть: ',
    lambda a: a > 0)
recursion(INP)