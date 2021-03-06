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
import time
import timeit
import math

def my_timeit(statements, mode=0):
    """
    Необходима библиотека import timeit

    Функция рассчитывает время исполнения алгоритма.
    Ключевое предположение, что прошлые запуски алгоритма не влияют на последующие, иначе функция
    будет работать некорректно. Например, если вы измеряете скорость выполнения mylist.sort().

    В функцию передается:
       1. statements - перечень функций с параметрами в виде списка. Например:
            а) statements = ['some_slow_method(5)',
                  'some_slow_method(3)',
                  'some_quick_method(5)',
                  'some_quick_method(3)']
            б) N=str(5)
               M=str(3)
               statements = ['some_slow_method(' + N + ')',
                  'some_slow_method(' + M + ')',
                  'some_quick_method(' + N + ')',
                  'some_quick_method(' + M + ')']
       2. mode - режим вывода:
            0 - вывод на экран
            1 - вывод в словарь


    """
    # проверка режима вывода

    # вывод на экран
    if mode == 0:
        # перебираем все функции из списка
        for item in statements:
            # в парметре setup метода timeit нужно название функции без скобок
            # (т.е. ссылка на функцию)
            setup = "from __main__ import " + item[: item.find("(")]
            # выводим результат текущей функции
            print(
                f'{item} выполняется за '
                f'{min(timeit.repeat(item, setup, timeit.default_timer, 3, 1))} секунд(ы)')
        ret = None
    # вывод в словарь
    elif mode == 1:
        # создаем словарь
        memory = {}
        # перебираем все функции из списка
        for item in statements:
            # в парметре setup метода timeit нужно название функции без скобок
            # (т.е. ссылка на функцию)
            setup = "from __main__ import " + item[: item.find("(")]
            # сохраняем результат в словарь
            memory[item] = min(
                timeit.repeat(
                    item,
                    setup,
                    timeit.default_timer,
                    3,
                    1))
        ret = memory
    else:
        print(f"Режим работы может быть:\n    0 - вывод на экран\n    1 - вывод в словарь")
        ret = None
    return ret
# --------------------------------------------------------------------------------------------------


def o_notation(func_start, func_end, iter_start, iter_end):
    """
    Необходима библиотека import math

    Функция определяет примерный тип сложности алгоритма.

    func_start - строка, содержащая вызов функции с начальными входными параметрами
    func_end - строка, содержащая вызов функции с конечными входными параметрами
    iter_start - начальное значение итерируемого аргумента функции
    iter_end - конечное значение итерируемого аргумента функции


    Примеры вызова функции:
        1) o_notation('some_quick_method(5)', 'some_quick_method(10)', 5, 10)
        2) N=5
           M=10
           func_start =  'some_quick_method(arg_1, arg_2, ..., arg_k, ' + str(N) + ')'
           func_end =  'some_quick_method(arg_1, arg_2, ..., arg_k, ' + str(M) + ')'
           o_notation(func_start, func_end, n, m)

    Используются типовые порядки роста сложности алгоритма:
        1. O(1)         - константная сложность
        2. O(log n)     – логарифмическая сложность
        3. O(n)         – линейная сложность
        4. O(n*log n)   - линеарифметическая сложность
        5. O(n**2)      – квадратичная сложность
        6. O(n**3)      – кубическая сложность
        7. O(e**n)      – экспоненциальная сложность

    Примерный тип сложности определяется исходя из времени выполнения алгоритма на разных
    входных данных. Полученные данные времени выполнения сверяются с графиками типовых порядков
    роста и выбирается самый ближний. Подразумевается, что алгоритм непрерывен.
    Начальная точка всех графиков считается (0,0).

    Если в системе координат шкалу оси x (итерируемый параметр) брать в соостветствии с функцией
    порядка роста сложности алгоритма (например 1, log(n), n ...), то результаты
    замеров времени данного алгоритма на разных входных данных должны быть очень близки к
    прямой линии. Соответсвенно, по первому времени выполнения рассчитываем угловой коэффициент
    прямой из начала координат и экстраполируем по этому расчету ожидаемое время выполнения
    алгоритма для второго значения итерируемого аргумента. Для той системы координат, для которой
    расчетное время будет ближе всего к фактическому, к той функции и стремится сложность алгоритма.

    Данный метод имеет право на жизнь, т.к. прямой метод ручного расчета сложности алгоритма также
    дает лишь оценочную функцию. Расчет верен, например только до тех пор, пока операцию
    сложения можно считать атомарной. На больших числах, которыми процессор не может оперировать
    непосредственно (например, загрузить в регистры и выполнить инструкцию add), суммирование
    не является атомарной операцией и начинает зависеть от количества разрядов в числе.
    А оно зависит от n – в результате алгоритм имеет более высокую, чем расчетная,
    вычислительную сложность на больших n.

    """

    # создаем словарь, в котором будут содержаться данные угловых коэффициентов
    # функций порядка роста
    memory = {
        'O(1)': 0,
        'O(log n)': 0,
        'O(n)': 0,
        'O(n*log n)': 0,
        'O(n**2)': 0,
        'O(n**3)': 0,
        'O(e**n)': 0
    }

    # вызываем функцию измерения времени работы алгоритма my_timeit() в режиме
    # вывода результатов в словарь

    # импортируем данные вызова в специальную переменную
    statements = [func_start,
                  func_end]
    # вызываем функцию и сохраняем результат в переменную res
    res = my_timeit(statements, 1)

    # полученные результаты замеров сохраняем из словаря res в переменные,
    # исключительно для удобства читаемости кода
    time_1 = res[func_start]
    time_2 = res[func_end]

    # считаем угловые коэффициенты прямых между точками (0,0)->(f(iter_start), time_1) и
    # рассчитываем ожидаемое значение времени в точке f(iter_end) в системах координат,
    # где шкала оси x соответствует каждой из функций потенциальных порядков роста
    # сложности алгоритма.
    # Сохраняем модуль разницы фактического time_2 и расчетного time_2 в словаре memory
    # в ключе соответствующего названия.
    # начальная точка (0,0), значит коэффициент равен t/f(x), расчетное time_2'=t/f(x)*f(x2),
    # а их разница: time_2-time_2'.
    # x1 - iter_start; x2 - iter_end
    # time_1 - res[func_start]; time_2 - res[func_end]
    memory['O(1)'] = abs(time_1 - time_2)
    memory['O(log n)'] = abs(
        time_2 -
        time_1 /
        math.log2(
            iter_start) *
        math.log2(
            iter_end))
    memory['O(n)'] = abs(time_2 - time_1 / iter_start * iter_end)
    memory['O(n*log n)'] = abs(time_2 - time_1 / (math.log2(iter_start)
                                                  * iter_start) * (math.log2(iter_end)
                                                                   * iter_end))
    memory['O(n**2)'] = abs(time_2 - time_1 / (iter_start**2) * (iter_end**2))
    memory['O(n**3)'] = abs(time_2 - time_1 / (iter_start**3) * (iter_end**3))
    try:
        memory['O(e**n)'] = abs(time_2 - time_1 /
                            math.exp(iter_start) * math.exp(iter_end))
    except:
        # заполняем большим значением
        memory['O(e**n)'] = 10000
        print (f"O(e**n) не оценено, слишком большие данные")

    # min(memory, key=memory.get) выдает ключ минимального значения словаря, но используем цикл
    # причину смотрим в task_1_3.py
    # print(
    #    f"Порядок роста сложности алгоритма {func_start[: func_start.find('(')]}: "
    #    f"{min(memory, key=memory.get)}")
    min_key = 'O(1)'
    min_val = memory[min_key]
    for key, val in memory.items():
        if val < min_val:
            min_val = val
            min_key = key
    print(
        f"Порядок роста сложности алгоритма {func_start[: func_start.find('(')]}: "
        f"{min_key}")

# --------------------------------------------------------------------------------------------------
# блок тестовых функций


def some_very_slow_method(loop_count):
    """
    # эмуляция n**3
    """
    for i in range(loop_count):
        for j in range(loop_count):
            for trd in range(loop_count):
                time.sleep(0.01)
    return i + j + trd


def some_slow_method(loop_count):
    """
    # эмуляция n**2
    """
    for i in range(loop_count):
        for j in range(loop_count):
            time.sleep(0.01)
    return i + j

def some_quick_method(loop_count):
    """
    # эмуляция n
    """
    for i in range(loop_count):
        time.sleep(0.1)
    return i

def some_very_quick_method(loop_count):
    """
    # эмуляция O(1)
    """
    time.sleep(0.1)
    return loop_count

def bin_srch_method(loop_count):
    """
    # эмуляция бинарного поиска
    """
    for i in range(int(math.log(loop_count, 2))):
        time.sleep(0.1)
    return i

def n_log_n_method(loop_count):
    """
    # эмуляция O(n*log n)
    """
    for i in range(int(math.log(loop_count, 2) * loop_count)):
        time.sleep(0.1)
    return i

def e_n_method(loop_count):
    """
    # эмуляция O(e**n), жутко долгий даже для тестовой функции
    """
    for i in range(int(math.exp(loop_count))):
        # time.sleep(0.1)
        const = 1
    return i + const

# --------------------------------------------------------------------------------------------------
# рабочий код

"""
N = 5
M = 10

START = 'some_very_quick_method(' + str(N) + ')'
END = 'some_very_quick_method(' + str(M) + ')'
o_notation(START, END, N, M)

START = 'some_quick_method(' + str(N) + ')'
END = 'some_quick_method(' + str(M) + ')'
o_notation(START, END, N, M)

START = 'some_slow_method(' + str(N) + ')'
END = 'some_slow_method(' + str(M) + ')'
o_notation(START, END, N, M)

START = 'some_very_slow_method(' + str(N) + ')'
END = 'some_very_slow_method(' + str(M) + ')'
o_notation(START, END, N, M)

START = 'bin_srch_method(' + str(N) + ')'
END = 'bin_srch_method(' + str(M) + ')'
o_notation(START, END, N, M)

START = 'n_log_n_method(' + str(N) + ')'
END = 'n_log_n_method(' + str(M) + ')'
o_notation(START, END, N, M)

START = 'e_n_method(' + str(N) + ')'
END = 'e_n_method(' + str(M) + ')'
o_notation(START, END, N, M)
"""

# Результаты работы:
#     Порядок роста сложности алгоритма some_very_quick_method: O(1)
#     Порядок роста сложности алгоритма some_quick_method: O(n)
#     Порядок роста сложности алгоритма some_slow_method: O(n**2)
#     Порядок роста сложности алгоритма some_very_slow_method: O(n**3)
#     Порядок роста сложности алгоритма bin_srch_method: O(log n)
#     Порядок роста сложности алгоритма n_log_n_method: O(n*log n)
#     Порядок роста сложности алгоритма e_n_method: O(e**n)
# Совпадает
