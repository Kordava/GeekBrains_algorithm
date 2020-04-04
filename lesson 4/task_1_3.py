"""
1. Проанализировать скорость и сложность одного любого алгоритма,
разработанных в рамках домашнего задания первых трех уроков.
Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.

Подсказка:
1) возьмите 2-3 задачи, реализованные ранее, сделайте замеры на разных входных данных
2) сделайте для каждой из задач оптимизацию (придумайте что можно оптимизировать)
и также выполните замеры на уже оптимизированных алгоритмах
3) опишите результаты - где, что эффективнее и почему.

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО
"""

# --------------------------------------------------------------------------------------------------
# этап 3: оптимизация кода функции o_notation() из этапа 1.
import timeit
import math

# блок оптимизируемых функций

# 1. Поиск ключа минимального значения словаря----------------------------
MEMORY = {
    'O(1)': 2,
    'O(log n)': 4,
    'O(n)': 6,
    'O(n*log n)': 12,
    'O(n**2)': 34,
    'O(n**3)': 1,
    'O(e**n)': 8
}


def f_min():
    """# через функцию min()"""
    res = min(MEMORY, key=MEMORY.get)
    return res


def f_for():
    """# через цикл"""
    min_val = MEMORY['O(1)']
    for key, val in MEMORY.items():
        if val < min_val:
            min_val = val
            min_key = key

    res = min_key
    return res


def f_list():
    """ # через список
        a) create a list of the dict keys and values;
        b) return the key with the max value"""
    val_list = list(MEMORY.values())
    keys_list = list(MEMORY.keys())
    return keys_list[val_list.index(min(val_list))]


# проверяем
SETUP = "from __main__ import f_min, f_for, f_list"
FUNC = 'f_min()'
print(
    f'f_min выполняется за {timeit.timeit(FUNC, setup=SETUP, number=1000)} секунд(ы)')
FUNC = 'f_for()'
print(
    f'f_for выполняется за {timeit.timeit(FUNC, setup=SETUP, number=1000)} секунд(ы)')
FUNC = 'f_list()'
print(
    f'f_list выполняется за {timeit.timeit(FUNC, setup=SETUP, number=1000)} секунд(ы)')

# результат
#   f_min выполняется за 0.0007495999999999996 секунд(ы)
#   f_for выполняется за 0.0005277999999999984 секунд(ы)
#   f_list выполняется за 0.0010704999999999985 секунд(ы)

# вывод: либо красота кода, либо эффективность. В данном случае речь идет об оптимизации,
# значит наш выбор f_for. Самый лаконичный f_min.

# 2. Математические функции-----------------------------------------------


def f_log():
    """# через функцию math.log(X, [base])"""
    res = math.log(10, 2)
    return res


def f_log2():
    """# через функцию math.log2(X)"""
    res = math.log2(10)
    return res


# проверяем
SETUP = "from __main__ import f_log, f_log2"
FUNC = 'f_log()'
print(
    f'f_log выполняется за {timeit.timeit(FUNC, setup=SETUP, number=1000)} секунд(ы)')
FUNC = 'f_log2()'
print(
    f'f_log2 выполняется за {timeit.timeit(FUNC, setup=SETUP, number=1000)} секунд(ы)')

# результат
#   f_log выполняется за 0.0004854999999999998 секунд(ы)
#   f_log2 выполняется за 0.00038900000000000046 секунд(ы)

# вывод: math.log2 и быстрее и компактнее.


def f_fabs():
    """# math.fabs(X)"""
    res = math.fabs(10)
    return res


def f_abs():
    """# через abs()"""
    res = abs(10)
    return res


# проверяем
SETUP = "from __main__ import f_fabs, f_abs"
FUNC = 'f_fabs()'
print(
    f'f_fabs выполняется за {timeit.timeit(FUNC, setup=SETUP, number=1000)} секунд(ы)')
FUNC = 'f_abs()'
print(
    f'f_abs выполняется за {timeit.timeit(FUNC, setup=SETUP, number=1000)} секунд(ы)')

# результат
#   f_fabs выполняется за 0.00019890000000000185 секунд(ы)
#   f_abs выполняется за 0.00010929999999999968 секунд(ы)

# вывод: abs() быстрее.
