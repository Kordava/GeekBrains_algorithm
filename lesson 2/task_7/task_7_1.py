"""
7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
где n - любое натуральное число.
"""
# из собственной библиотеки подключаю функцию контроля ввода числа
# функцию использовал в предыдущих работах, не буду загромождать
from lib import input_nbr

# код основной программы из задания
# пользователь вводит число
NUMB = input_nbr(
    'int',
    '> Введите натуральное числа для проверки равенства: ',
    lambda a: a > 0)

# переменная для хранения суммы ряда
SUM = 0

# считаем сумму ряда
for i in range(1, NUMB + 1):
    SUM += i

# сравниваем полученную сумму с формулой
if SUM == NUMB * (NUMB + 1) // 2:
    print(
        f"Все верно, сумма ряда и расчет формулы совпадают. "
        f"Сумма ряда из {NUMB} элементов равна {SUM}")
else:
    print(
        f"Не равны. Сумма ряда из {NUMB} элементов равна {SUM}, "
        f"формула дает {NUMB * (NUMB + 1) // 2}")
