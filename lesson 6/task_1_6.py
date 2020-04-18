"""
1.	Подсчитать, сколько было выделено памяти под переменные в ранее
разработанных программах в рамках первых трех уроков.
Проанализировать результат и определить программы с
наиболее эффективным использованием памяти.
Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько
вариантов кода для одной и той же задачи.
Результаты анализа вставьте в виде комментариев к коду.
Также укажите в комментариях версию Python и разрядность вашей ОС.


ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО
"""
# 1. Шестой шаг улучшения - полная оптимизация и генераторы, плюс не
# растут ресурсы от числа.

# 2. Результаты.
# Было
# Выполнение заняло 12.53125 сек и 635.1796875 Мб
# ert для 1000000: 15485867

# Вариант 2
# Выполнение заняло 8.921875 сек и 325.96484375 Мб
# ert для 1000000: 15485867

# Вариант 3
# Выполнение заняло 17.34375 сек и 2.12109375 Мб
# ert для 1000000: 15485863

# Вариант 4
# Выполнение заняло 23.328125 сек и 7.33984375 Мб
# ert для 1000000: 15485863

# Вариант 5
# Выполнение заняло 22.546875 сек и 0.54296875 Мб
# ert для 1000000: 15485863

# Вариант 6
# Выполнение заняло 1.5625 сек и 42.26953125 Мб
# 15485863

# Вариант 6
# не успел, но уже реализован в task_1_2

# Итог: на генераторах скорость работы в десятки раз выше, памяти от аналогичного
# по смыслу варианта 1 в 15 раз меньше.

# импортируем функцию замера времени работы из первого задания
import time
import memory_profiler


def primes(number):
    """
    вынесем расчет чисел в отдельную функцию. Применим все наработки сразу в расчетах: обнуление с
    квадрата числа, перебор до корня квадратного от границы, сохранять в массиве только ДА и НЕТ
    (можно что угодно, хоть 10 и 11), четные числа игнорируем, значения не нужны,
    совпадают с индексами. Используем генераторы, поэтому не знаю как применить numpy

    """
    my_list = [True] * number
    # диапазон чисел сразу ограничим корнем квадратным из границы, четные
    # числа игнорируем
    for i in range(3, int(number**0.5) + 1, 2):
        if my_list[i]:
            # перебор начинаем с квадрата числа, используем генератор
            my_list[i * i::2 * i] = [False] * \
                ((number - i * i - 1) // (2 * i) + 1)
    return [2] + [i for i in range(3, number, 2) if my_list[i]]


# начальные параметры замеров
TIME1 = time.process_time()
MEM1 = memory_profiler.memory_usage()

# номер искомого числа
I = 1000000
# Начальная длина ряда чисел
NUM = I * 2
while True:
    # получаем список простых чисел в диапазоне до NUM
    RES = primes(NUM)
    # количество простых чисел
    LEN_RES = len(RES)
    # если мало, увеличиваем диапазон
    if LEN_RES < I:
        NUM *= 2
    # иначе выходим из цикла
    else:
        break

# индекс искомого числа с конца
IND = LEN_RES - I + 1
print(RES[-IND])

TIME2 = time.process_time()
MEM2 = memory_profiler.memory_usage()
TIME_DIFF = TIME2 - TIME1
MEM_DIFF = MEM2[0] - MEM1[0]
print(f"Выполнение заняло {TIME_DIFF} сек и {MEM_DIFF} Мб")
