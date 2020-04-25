"""
тест сортировок
"""
import timeit
import random
from random import randint

# сравним время работы разных алгоритмов

#----------------------------------------------------------------------------------------------
# число чисел в массиве
I = 3000000
# выводим на экран для удобства
print(I)
# формируем массив
my_list = [randint(0,10000) for i in range(1,I)]

# -----------------------------------------------------------------------------------------
def my_sort_count_new_5(data):
    """
    Мой алгоритм сортировки
    """
    # будет содержать конечный вывод
    data2 = []
    # будет использована для поиска максимального числа в массиве
    # вначале равно первому элементы массива
    Nmax = data[0]
    # этот вспомогательный массив длиною до максимального числа во входящем массиве
    # в нем будем считать, сколько раз каждое из чисел входит в начальный массив
    my_work_list = [0] * (Nmax + 1)
    # идем по массиву
    for i in data:
        # если число больше максимального, расширяем длину вспомогательного массива до нового максимума
        # и обновляем переменную максимума
        if i > Nmax:
            my_work_list.extend([0] * (i - Nmax))
            Nmax = i
        # увеличиваем во вспомогательном массиве счеткик вхождения числа в начальный массив
        my_work_list[i] += 1
    # перебираем все числа до максимального и формируем новый массив, уже отсортированный
    for i in range(Nmax+1):
        data2.extend([i] * my_work_list[i])
    return data2

# копируем наш массив в новую переменную для предотвращения случайного изменения при дальнейшей работе
random_list_of_nums = list(my_list)
print(f'my_sort_count_new_5: {timeit.timeit("my_sort_count_new_5(random_list_of_nums)", setup="from __main__ import my_sort_count_new_5, random_list_of_nums", number=100)}')
#------------------------------------------------------------------------------------------------
'''
def bubble_sort_dec_new(orig_list):
    """Сортировка пузырьком, улучшенная, задание 1"""
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

# копируем наш массив в новую переменную для предотвращения случайного изменения при дальнейшей работе
random_list_of_nums = list(my_list)
print(f'bubble_sort_dec_new: {timeit.timeit("bubble_sort_dec_new(random_list_of_nums)", setup="from __main__ import bubble_sort_dec_new, random_list_of_nums", number=100)}')
'''
#-------------------------------------------------------------------------------------------
# встроенная функция
random_list_of_nums = list(my_list)
print(f'sorted: {timeit.timeit("sorted(random_list_of_nums)", setup="from __main__ import random_list_of_nums", number=100)}')
#----------------------------------------------------------------------------------------------
'''
def quick_sort(orig_list):
    """
    из урока
    """
    if len(orig_list) <= 1:
        return orig_list
    else:
        q = random.choice(orig_list)
        L = []
        M = []
        R = []
        for elem in orig_list:
            if elem < q:
                L.append(elem)
            elif elem > q:
                R.append(elem)
            else:
                M.append(elem)
        return quick_sort(L) + M + quick_sort(R)

random_list_of_nums = list(my_list)
print(f'quick_sort: {timeit.timeit("quick_sort(random_list_of_nums)", setup="from __main__ import quick_sort, random_list_of_nums", number=100)}')
'''
#----------------------------------------------------------------------------------------------
'''
def insertion_sort(orig_list):
    """
    из урока
    """
    for i in range(len(orig_list)):
        v = orig_list[i]
        j = i

        while (orig_list[j-1] > v) and (j > 0):

            orig_list[j] = orig_list[j-1]
            j = j - 1

        orig_list[j] = v
    return orig_list

random_list_of_nums = list(my_list)
print(f'insertion_sort: {timeit.timeit("insertion_sort(random_list_of_nums)", setup="from __main__ import insertion_sort, random_list_of_nums", number=100)}')
'''

"""
3000
my_sort_count_new_5: 0.2157589
bubble_sort_dec_new: 1.0482827
sorted: 0.03062599999999982
quick_sort: 0.9950916999999997
insertion_sort: 0.5619562999999999

30000
my_sort_count_new_5: 0.5770357
bubble_sort_dec_new: 97.0669666
sorted: 0.4308918999999918
quick_sort: 5.92450199999999
insertion_sort: 53.963932

bubble_sort_dec_new - вылетает, дальше без него
insertion_sort - вылетает, дальше без него

300000
my_sort_count_new_5: 4.5223629999999995
sorted: 6.737869699999999
quick_sort: 62.66195890000001

quick_sort - вылетает, дальше без него

3000000
my_sort_count_new_5: 42.7400399
sorted: 79.3770864

И чудеса бывают! На больших числах алгометрия выигрывает у компиляции! Ясно, что стандартная 
функция "широкая", но все же это дает задержку лишь на константу, на больших числах 
чистый алгоритм. 

Вывод: "узкие" библиотеки можно делать свои!



"""