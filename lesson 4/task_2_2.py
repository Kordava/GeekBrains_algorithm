"""
Написать два алгоритма нахождения i-го по счёту простого числа.
Без использования «Решета Эратосфена»;
Используя алгоритм «Решето Эратосфена»

Подсказка:
Сравните алгоритмы по времени на разных порядковых номерах чисел:
10, 100, 1000
Опишите результаты, сделайте выводы, где и какой алгоритм эффективнее
Подумайте и по возможности определите сложность каждого алгоритма

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО
"""

# импортируем функцию замера времени работы из первого задания
from lib import my_timeit
from lib import o_notation

# рабочая область---------------------------------------------------------
# Блок 2. С решетом-------------------------------------------------------


def ert_old(iter1):
    """
    Реализация алгоритма
    Решето Эратосфена

    Начальная версия.

    Основная проблема - алгоритм работает на заданном множисте. А его мы не имеем,
    нет правой границы диапазона. Значит придется иетрировать.

    iter1 - порядковый номер простого числа, которое требуется найти (входной параметр)
    """
    # мы не знаем, сколько простых чисел в каком диапазоне,
    # но можем оценить. Половина четных чисел отпадает сразу, втрое простое число - 3. В сотне его
    # 33 штуки, за минусом половины четным грубо имеем 15. То, есть 65 чисел из 100 точно
    # не простые. Чуть меньше третьей части. Возьмем коэффициент 2, итерация все равно придет к
    # нужному числу. Плюс придется делать меньше лишних обнулений правой
    # границы.
    num = iter1 * 2
    # счетчик простых чисел
    count = 0
    # счетчик чисел диапазона
    i = 0
    # ряд натуральных чисел до заданного
    my_list = list(range(num + 1))
    # без этой строки итоговый список будет содержать единицу
    my_list[1] = 0
    # будем итерерировать пока не найдем заданное число
    while True:
        # переходим к следующему числу
        i += 1
        # для 1 значение уже ввели
        if i > 1:
            # если достигли границы диапазона, но нужное число не нашли
            if i > num:
                # обнуляем счетчик ряда
                i = 0
                # расширяем диапазон поиска в два раза
                num *= 2
                # заново формируем массив чисел
                my_list = list(range(num + 1))
                # обнуляем счетчик простых чисел
                count = 0
                # переходим на следующую итерацию цикла с новыми значениями
                continue
            # если значение этого элемента нашего массива равно нулю, значит оно было
            # кратно одному из предыдущих членов массива и уже обнулилось. Поэтому это число самое
            # левое из ряда необработанных чисел, поэтому оно простое
            if my_list[i] != 0:
                # увеличиваем счетчик
                count += 1
            # если нужное нам число, возвращаем его и выходим
            if count == iter1:
                return i
            # если до нужного еще не дошли, то убираем заведомо составные числа из правого
            # края массива. Идем по ряду с шагом i (кратным нашему числу),
            # тем самым обнуляя все элементы, кратные i.
            for j in range(i, num, i):
                my_list[j] = 0

# ------------------------------------------------------------------------------------------------
def ert(iter1):
    """
    Реализация алгоритма
    Решето Эратосфена

    Конечная версия.

    Основная проблема - алгоритм работает на заданном множисте. А его мы не имеем,
    нет правой границы диапазона. Значит придется иетрировать.

    iter - порядковый номер простого числа, которое требуется найти (входной параметр)
    """
    # мы не знаем, сколько простых чисел в каком диапазоне,
    # но можем оценить. Половина четных чисел отпадает сразу, втрое простое число - 3. В сотне его
    # 33 штуки, за минусом половины четным грубо имеем 15. То, есть 65 чисел из 100 точно
    # не простые. Чуть меньше третьей части. Возьмем коэффициент 2, итерация все равно придет к
    # нужному числу. Плюс придется делать меньше лишних обнулений правой
    # границы.
    num = iter1 * 2
    # счетчик простых чисел
    count = 0
    # счетчик чисел диапазона
    i = 0
    # ряд натуральных чисел до заданного
    my_list = list(range(num + 1))
    # без этой строки итоговый список будет содержать единицу
    my_list[1] = 0
    # будем итерерировать пока не найдем заданное число
    while True:
        # переходим к следующему числу
        i += 1
        # для 1 значение уже ввели
        if i > 1:
            # если достигли границы диапазона, но нужное число не нашли
            if i > num:
                # обнуляем счетчик ряда
                i = 0
                # расширяем диапазон поиска в два раза
                num *= 2
                # заново формируем массив чисел
                my_list = list(range(num + 1))
                # обнуляем счетчик простых чисел
                count = 0
                # переходим на следующую итерацию цикла с новыми значениями
                continue
            # 1. Улучшение. Если значение этого элемента нашего массива равно нулю,
            # значит оно было кратно одному из предыдущих членов массива и уже обнулилось.
            # Поэтому и все остальные элементы кратные это му числу уже заведомо обнулены.
            # Прерываемся и перходим к следующему
            if my_list[i] == 0:
                continue
            # Вот тут важный момент! В этой области могут быть уже только простые числа i.
            # Сложные уже отсеялись на прошлом шаге и обнулены. Тут мы имеем дело с очередным
            # простым числом и будем удалять вправо кратные ему числа. Слева от него или нули, или
            # простые. Поэтому увеличиваем счетчик простых чисел
            count += 1
            # если нужное нам число, возвращаем его и выходим
            if count == iter1:
                return i
            # если до нужного еще не дошли, то убираем заведомо составные числа из правого
            # края массива. Идем по ряду с шагом i (кратным нашему числу),
            # тем самым обнуляя все элементы, кратные i.
            #
            # 2. улучшение - начинаем с элемента i в квадрате,
            # так как идем по возрастанию и остальные элементы обнулены от
            # предыдущих чисел.

            for j in range(i ** 2, num, i):
                my_list[j] = 0
# ------------------------------------------------------------------------------------------------

# вперед

# порядковый номер искомого простого числа
I = 100000

print(f"ert для {I}: {ert(I)}")
print(f"ert_old для {I}: {ert_old(I)}")

# импортируем данные вызова в специальную переменную
STATEMENTS = ['ert_old(' + str(I) + ')',
              'ert(' + str(I) + ')']
# вызываем функцию расчета времени выполнения
my_timeit(STATEMENTS)

# оценим тип сложности алгоритмов
N = 10
M = 1000
START = 'ert_old(' + str(N) + ')'
END = 'ert_old(' + str(M) + ')'
o_notation(START, END, N, M)

START = 'ert(' + str(N) + ')'
END = 'ert(' + str(M) + ')'
o_notation(START, END, N, M)

# результаты
#    ert для 10000: 104729
#    ert_old для 10000: 104729
#    ert_old(10000) выполняется за 0.3123043 секунд(ы)
#    ert(10000) выполняется за 0.0864163 секунд(ы)
#    O(e**n) не оценено, слишком большие данные
#    Порядок роста сложности алгоритма ert_old: O(n*log n)
#    O(e**n) не оценено, слишком большие данные
#    Порядок роста сложности алгоритма ert: O(n*log n)

#    Process finished with exit code 0

# Вывод: оптимизация ускорила функцию в разы, но при этом порядок сложности не изменился и
# близок к n*log(n). Формально, мы имеем два вложенных цикла - n**2, но это не так. Второй цикл не
# обрабатывает уже обнуленные числа, а их очень много. Оставшиеся простые чмсла
# пропорциональны log(n) (или даже log(log(n)) так как начинаем с квадрата числа и оставшихся чисел
# пропорционально log(n)). Но в нашем случае это не важно, числа ожидаются большие и логика работы
# ЭВМ на больших числах алгоритм сильно усложнит без нас

# результаты стандартного алгоритма из модуля task_2_1
#    simple_old для 3000: 27449
#    simple для 3000: 27449
#    simple_old(10000) выполняется за 37.641572100000005 секунд(ы)
#    simple(10000) выполняется за 0.16210440000000403 секунд(ы)
#    O(e**n) не оценено, слишком большие данные
#    Порядок роста сложности алгоритма simple_old: O(n**2)
#    O(e**n) не оценено, слишком большие данные
#    Порядок роста сложности алгоритма simple: O(n*log n)
# Process finished with exit code 0

# Общий вывод
# _______________________________________________________________________________________________
# Обе оптимизированные функции имеют схожий порядок сложности - O(n*log n).
# На сравнимых данных алгоритм Ератосфера работает на константу быстрее, на больших числах должен
# уходить вперед за счет log(log(n), если не вмешается логика ЭВМ. К тому же алгоритм Эратосфера
# можно еще улучшить за счет не обнуления списка, а добавления новых данных справа, по прикидкам
# тогда точно выйдем в nlog(log(n)), но не успею уже. Проверим на неприлично больших числах? Вперед!

#    ert(10000000) выполняется за 267.2714780000001 секунд(ы)
#    Порядок роста сложности алгоритма ert: O(n*log n) - (шаблона на n*log(log(n)) пока нет, скорее
#       всего n*log(log(n))

#    simple(100000) выполняется за 6.6460452 секунд(ы)
#    simple(1000000) выполняется за 214.63450520000004 секунд(ы)
#    Порядок роста сложности алгоритма simple: O(n*log n)

# Минус Эратосфера - ест ресурсы. Стандартный алгоритм не требует таких ресурсов, его специфика в
# единичной проверке каждого числа и сохранении нужного. Таких массивов данных нет. Думаю на
# больших числах для слабого компьютера Эратосфер не подойдет.
# Но скорость работы! На порядки выше, все же он выходит в свои n*log(log(n)). И на больших цифрах
# это очевидно. На десяти миллонах время выполнения решета как у стандартного на миллионе.
# Стандартный на десять миллионов не дождался, по прикидкам разница будет раз в 80.
"""
# импортируем данные вызова в специальную переменную
STATEMENTS = ['ert(' + str(I) + ')']
# вызываем функцию расчета времени выполнения
my_timeit(STATEMENTS)

# оценим тип сложности алгоритмов
N = 100
M = 100000
START = 'ert_old(' + str(N) + ')'
END = 'ert_old(' + str(M) + ')'
o_notation(START, END, N, M)

START = 'ert(' + str(N) + ')'
END = 'ert(' + str(M) + ')'
o_notation(START, END, N, M)
"""
