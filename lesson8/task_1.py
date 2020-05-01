"""
1. Определение количества различных подстрок с использованием хэш-функции.
Пусть дана строка S длиной N, состоящая только из маленьких латинских букв.
Требуется найти количество различных подстрок в этой строке.
"""
import hashlib


def line_count(work_list):
    '''
    Сразу оговоримся, что алгоритмы хэширования строк имеют большой недостаток:
    они не 100%-ны, есть множество строк, хэши которых совпадают.
    Если речь идет об осмысленном тексте, то подобрать текст с таким же значением
    хэша крайне трудно и вероятность совпадения хэшей очень мала.
    Если, как в данном задании, речь идет о произвольной строке, то применение хэша,
    с моей точки зрения, не корректно, реальное количество уникальных подстрок может быть больше,
    чем хэшей. То есть полученная величина оценочная, как нижняя грань
    '''
    # сохраним длину нашей строки в переменную, чтобы не считать каждый раз
    len_sub = len(work_list)
    # пустую строку тоже посчитаем вариантом
    if len_sub < 2:
        return 1
    # в списке будут хранится хэши подстрок
    h_subs = []
    # берем отрезки длиной 1 - длина списка
    for i in range(len_sub + 1):
        # движемся по списку отрезками длиной i
        for j in range(len_sub - i + 1):
            # добавляем хэш каждого отрезка в наш массив
            h_subs.append(hashlib.sha1(
                work_list[j:i + j].encode('utf-8')).hexdigest())
    # считаем количество уникальных хэшей, дубли удалим через множество set()
    res = len(set(h_subs))
    return res


# в данном случае имеем 276 вариантов всего и 198 уникальных
print(line_count('assasaasasssssssaaaasa'))
