"""
2.	Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры
(4, 6 и 0) и 2 нечетные (3 и 5).

Подсказка:
Для извлечения цифр числа используйте арифм. операции

Пример:
Введите натуральное число: 44
В числе 44 всего 2 цифр, из которых 2 чётных и 0 нечётных
"""
# из собственной библиотеки подключаю функцию контроля ввода числа
# функцию использовал в предыдущих работах, не буду загромождать
from lib import input_nbr

# содержит код основной программы из задания


def main():
    """
        содержит код основной программы из задания
    """
    # пользователь вводит число
    inp = input_nbr(
        'int',
        '> Введите натуральное число: ',
        lambda a: a > 0)
    # сохраним введенное число во временную переменную
    numb = inp
    # счетчики четных, нечетных, всего цифр в числе
    even = odd = total = 0
    while numb > 0:
        if numb % 2 == 0:
            even += 1
        else:
            odd += 1
        numb //= 10
        total += 1
    print(
        f"В числе {inp} всего {total} цифр, из которых {even} чётных и {odd} нечётных")


# ЭТО СОБСТВЕННО ВЫЗОВ КОДА ПРОГРАММЫ
main()                                  # ну, вперед!
# конец кода программы////////////////////////////////////////////////////