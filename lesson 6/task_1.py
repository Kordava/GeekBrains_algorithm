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
# импортируем функцию замера времени работы из первого задания
import time
import memory_profiler
# ------------------------------------------------------------------------------------------------
# 0. самая ресурсоемкая задача из предыдущих заданий - поиск i-го простого числа через
# "решето". Ей и займемся.

# 1. @profile. Задача настолько ресурсоемкая, что @profile умирает прямо сразу. На поиске
# миллионного числа программа работает 12 секунд, вместе с @profile сразу смерть. На 100 000
# @profile еще тянет, но оооочень долго и со скрипом.

# 2. Придется обходиться прямым замером (спасибо примеру из вэбинара!
# честно использовал код примера):
#    t1 = time.process_time()
#    mem1 = memory_profiler.memory_usage()
#
#    замеряемая функция
#
#    time2 = time.process_time()
#    mem2 = memory_profiler.memory_usage()
#
#    time_diff = time2 - t1
#    mem_diff = mem2[0] - mem1[0]
#    print(f"Выполнение заняло {time_diff} сек and {mem_diff} Мб")
# Но! При выносе замеров из тела функции оспользование памяти расчитывается почти нулевым, тогда
# как в теле функции оно очень велико. Значит будем мерить внутри функции. Я так понимаю, что
# при выходе из функции локальные переменные зачищаются. Плюс заодно и время работы посчитаем,
# я так мыслю, что сваливание в своп резко увеличит время работы (WIN 10,
# 64 разряда, 16Гб памяти).

# 3. В идеале ставим задачу реализовать алгоритм, не зависящий от оперативной памяти компьютера.
# "Решето" любит ресурсы, а мы будем жадничать.

# 4. Первичный замер работы исходного алгоритма:
# Выполнение заняло 12.53125 сек и 635.1796875 Мб
# ert для 1000000: 15485863

# @profile


def ert(iter1):
    """
    Реализация алгоритма
    Решето Эратосфена

    Конечная версия.

    Основная проблема - алгоритм работает на заданном множисте. А его мы не имеем,
    нет правой границы диапазона. Значит придется иетрировать.

    iter - порядковый номер простого числа, которое требуется найти (входной параметр)
    """
    time1 = time.process_time()
    mem1 = memory_profiler.memory_usage()
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
                my_list[1] = 0
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
                time2 = time.process_time()
                mem2 = memory_profiler.memory_usage()
                time_diff = time2 - time1
                mem_diff = mem2[0] - mem1[0]
                print(f"Выполнение заняло {time_diff} сек и {mem_diff} Мб")
                return i
            # если до нужного еще не дошли, то убираем заведомо составные числа из правого
            # края массива. Идем по ряду с шагом i (кратным нашему числу),
            # тем самым обнуляя все элементы, кратные i.
            #
            # 2. улучшение - начинаем с элемента i в квадрате,
            # так как идем по возрастанию и остальные элементы обнулены от
            # предыдущих чисел.
            for j in range(i ** 2, num + 1, i):
                my_list[j] = 0
# ------------------------------------------------------------------------------------------------

# вперед


# порядковый номер искомого простого числа
I = 1000000
print(f"ert для {I}: {ert(I)}")
