"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы. Сортировка должна быть реализована в
виде функции. Обязательно доработайте алгоритм (сделайте его умнее).
Идея доработки: если за проход по списку не совершается ни одной сортировки, то завершение
Обязательно сделайте замеры времени обеих реализаций

Подсказка: обратите внимание, сортируем не по возрастанию, как в примере,
а по убыванию
"""
import timeit
import random

"""Сортировка пузырьком"""
# https://cdn.tproger.ru/wp-content/uploads/2017/09/BubbleSort.gif





def bubble_sort_dec(orig_list):
    """Сортировка пузырьком"""
    num = 1
    # пока длина не отсортированного участка меньше длины массива
    while num < len(orig_list):
        # проходим не отсортированный участок
        for i in range(len(orig_list) - num):
            # если предыдущий меньше следующего, то меняем местами
            if orig_list[i] < orig_list[i + 1]:
                orig_list[i], orig_list[i + 1] = orig_list[i + 1], orig_list[i]
         # укорачиваем длину не отсортированного массива
        num += 1
    return orig_list


def bubble_sort_dec_new(orig_list):
    """Сортировка пузырьком"""
    num = 1
    # если будет истина, то массив отсортирован
    break_point = False
    # пока длина не отсортированного участка меньше длины массива
    while num < len(orig_list):
        # проходим не отсортированный участок
        for i in range(len(orig_list) - num):
            # если предыдущий меньше следующего, то меняем местами
            if orig_list[i] < orig_list[i + 1]:
                orig_list[i], orig_list[i + 1] = orig_list[i + 1], orig_list[i]
                break_point = True
        # если не сделано ни одной перестановки, то массив отсортирован
        if not break_point:
            break
        break_point = False
        # укорачиваем длину не отсортированного массива
        num += 1
    return orig_list


# генерируем массив
ORIG_LIST_10 = [random.randint(-100, 100) for _ in range(10)]
# выводим на экран
print(f'Оригинальный массив: {ORIG_LIST_10}')
# копируем наш массив в новую переменную для предотвращения сортировки
# второй функцией уже отсортированного массива (кстати так и выходит, функция работая с массивом
# оставляет глобальный масив отсортированным)
RANDOM_LIST_OF_NUMS = list(ORIG_LIST_10)
# выводим результаты обеих функций для проверки
print(
    f'Результат оригинальной функции: {bubble_sort_dec(RANDOM_LIST_OF_NUMS)}')
RANDOM_LIST_OF_NUMS = list(ORIG_LIST_10)
print(
    f'Результат улучшенной функции:   {bubble_sort_dec_new(RANDOM_LIST_OF_NUMS)}')

# замеры 10
print(f'Замеры 10 эллементов')
RANDOM_LIST_OF_NUMS = list(ORIG_LIST_10)
# python не дал перенести содержимое {}. Autopep тоже не смог. Вопрос для
# разбора
print(f'bubble_sort_dec: {timeit.timeit("bubble_sort_dec(RANDOM_LIST_OF_NUMS)", setup="from __main__ import bubble_sort_dec, RANDOM_LIST_OF_NUMS", number=1000)}')
RANDOM_LIST_OF_NUMS = list(ORIG_LIST_10)
print(f'bubble_sort_dec_new: {timeit.timeit("bubble_sort_dec_new(RANDOM_LIST_OF_NUMS)", setup="from __main__ import bubble_sort_dec_new, RANDOM_LIST_OF_NUMS", number=1000)}')


# замеры 100
ORIG_LIST_100 = [random.randint(-100, 100) for _ in range(100)]
print(f'Замеры 100 эллементов')
RANDOM_LIST_OF_NUMS = list(ORIG_LIST_100)
print(f'bubble_sort_dec: {timeit.timeit("bubble_sort_dec(RANDOM_LIST_OF_NUMS)", setup="from __main__ import bubble_sort_dec, RANDOM_LIST_OF_NUMS", number=1000)}')
RANDOM_LIST_OF_NUMS = list(ORIG_LIST_100)
print(f'bubble_sort_dec_new: {timeit.timeit("bubble_sort_dec_new(RANDOM_LIST_OF_NUMS)", setup="from __main__ import bubble_sort_dec_new, RANDOM_LIST_OF_NUMS", number=1000)}')


# замеры 1000
ORIG_LIST_1000 = [random.randint(-100, 100) for _ in range(1000)]
# print(ORIG_LIST)
print(f'Замеры 1000 эллементов')
RANDOM_LIST_OF_NUMS = list(ORIG_LIST_1000)
print(f'bubble_sort_dec: {timeit.timeit("bubble_sort_dec(RANDOM_LIST_OF_NUMS)", setup="from __main__ import bubble_sort_dec, RANDOM_LIST_OF_NUMS", number=1000)}')
RANDOM_LIST_OF_NUMS = list(ORIG_LIST_1000)
# print(RANDOM_LIST_OF_NUMS)
print(f'bubble_sort_dec_new: {timeit.timeit("bubble_sort_dec_new(RANDOM_LIST_OF_NUMS)", setup="from __main__ import bubble_sort_dec_new, RANDOM_LIST_OF_NUMS", number=1000)}')
# print(f'{bubble_sort_dec_new(RANDOM_LIST_OF_NUMS)}')

"""
Оригинальный массив: [-72, 35, -55, -84, -73, -95, 4, 39, -73, -89]
Результат оригинальной функции: [39, 35, 4, -55, -72, -73, -73, -84, -89, -95]
Результат улучшенной функции:   [39, 35, 4, -55, -72, -73, -73, -84, -89, -95]
Замеры 10 эллементов
bubble_sort_dec: 0.016272300000000003
bubble_sort_dec_new: 0.0032294000000000003
Замеры 100 эллементов
bubble_sort_dec: 0.5006896000000001
bubble_sort_dec_new: 0.008816200000000052
Замеры 1000 эллементов
bubble_sort_dec: 44.407858000000004
bubble_sort_dec_new: 0.17201259999999507
"""
