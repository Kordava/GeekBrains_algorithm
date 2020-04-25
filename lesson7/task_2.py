"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.

Пример:
Введите число элементов: 5
Исходный - [46.11436617832828, 41.62921998361278, 18.45859540989644, 12.128870723745806, 8.025098788570562]
Отсортированный - [8.025098788570562, 12.128870723745806, 18.45859540989644, 41.62921998361278, 46.11436617832828]
"""
import timeit

# Вариант 1---------------------------------------------------------------


def merge_sort_2(nums):
    """
    Вариант 1

    """
    # Возвращаем список, если он состоит из одного элемента
    if len(nums) <= 1:
        return nums

    # Для того чтобы найти середину списка, используем деление без остатка
    # Индексы должны быть integer
    mid = len(nums) // 2

    # Сортируем и объединяем подсписки
    left_list = merge_sort_2(nums[:mid])
    right_list = merge_sort_2(nums[mid:])

    # Объединяем отсортированные списки в результирующий
    return merge(left_list, right_list)


def merge(left_list, right_list):
    """
    Вспомогательная функция
    Как на уроке работает без нее не очень понял

    """
    sorted_list = []
    left_list_index = right_list_index = 0

    # Длина списков часто используется, поэтому создадим переменные для
    # удобства
    left_list_length, right_list_length = len(left_list), len(right_list)

    for _ in range(left_list_length + right_list_length):
        if left_list_index < left_list_length and right_list_index < right_list_length:
            # Сравниваем первые элементы в начале каждого списка
            # Если первый элемент левого подсписка меньше, добавляем его
            # в отсортированный массив
            if left_list[left_list_index] <= right_list[right_list_index]:
                sorted_list.append(left_list[left_list_index])
                left_list_index += 1
            # Если первый элемент правого подсписка меньше, добавляем его
            # в отсортированный массив
            else:
                sorted_list.append(right_list[right_list_index])
                right_list_index += 1

        # Если достигнут конец левого списка, элементы правого списка
        # добавляем в конец результирующего списка
        elif left_list_index == left_list_length:
            sorted_list.append(right_list[right_list_index])
            right_list_index += 1
        # Если достигнут конец правого списка, элементы левого списка
        # добавляем в отсортированный массив
        elif right_list_index == right_list_length:
            sorted_list.append(left_list[left_list_index])
            left_list_index += 1

    return sorted_list

# Вариант с урока --------------------------------------------------------


def merge_sort(orig_list):
    """
    Вариант, разобранный на уроке

    """
    if len(orig_list) > 1:
        center = len(orig_list) // 2
        left = orig_list[:center]
        right = orig_list[center:]

        merge_sort(left)
        merge_sort(right)

        # перестали делить
        # выполняем слияние
        i, j, k = 0, 0, 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                orig_list[k] = left[i]
                i += 1
            else:
                orig_list[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            orig_list[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            orig_list[k] = right[j]
            j += 1
            k += 1
    # сместил в глобальную область, иначе теряем массив из одного эллемента
    return orig_list


ARRAY = [46.11436617832828, 41.62921998361278, 18.45859540989644, 12.128870723745806, 8.025098788570562]
print(ARRAY)

RANDOM_LIST_OF_NUMS = list(ARRAY)
print("Вариант 1")
print(
    timeit.timeit(
        "merge_sort_2(RANDOM_LIST_OF_NUMS)",
        setup="from __main__ import merge_sort_2, RANDOM_LIST_OF_NUMS",
        number=1000))
print(merge_sort_2(RANDOM_LIST_OF_NUMS))

print("Вариант с урока")
RANDOM_LIST_OF_NUMS = list(ARRAY)
print(
    timeit.timeit(
        "merge_sort(RANDOM_LIST_OF_NUMS)",
        setup="from __main__ import merge_sort, RANDOM_LIST_OF_NUMS",
        number=1000))
print(merge_sort(RANDOM_LIST_OF_NUMS))

"""
[78, 41, 4, 27, 3, 27, 8, 39, 19, 34, 6, 41, 13, 52, 16]
Вариант 1
0.0249456
[3, 4, 6, 8, 13, 16, 19, 27, 27, 34, 39, 41, 41, 52, 78]
Вариант с урока
0.0243006
[3, 4, 6, 8, 13, 16, 19, 27, 27, 34, 39, 41, 41, 52, 78]

Вариант 1
0.0062322
[8.025098788570562, 12.128870723745806, 18.45859540989644, 41.62921998361278, 46.11436617832828]
Вариант с урока
0.0056375999999999996
[8.025098788570562, 12.128870723745806, 18.45859540989644, 41.62921998361278, 46.11436617832828]

Вариант с лекции быстрее. Я так думаю, за счет циклов while вместо for
"""
