"""
Задание 3. По введенным пользователем координатам двух
точек вывести уравнение прямой,
проходящей через эти точки.

Подсказка:
Запросите у пользователя значения координат X и Y для первой и второй точки
Найдите в учебнике по высшей математике формулы расчета:
k – угловой коэффициент (действительное число), b – свободный член (действительное число)
Сформируйте уравнение прямой по формуле: y = kx + b – функция общего вида

Пример:
X1_VAL = 2, Y1_VAL = 3, X2_VAL = 4, Y2_VAL = 5
Уравнение прямой, проходящей через эти точки: y = 1.0x + 1.0
"""


def input_nbr(nbr_type, nbr_text, nbr_cond):
    """Проверяет, что пользователь ввел число с заданным условием.

        Именованные параметры:
        nbr_type        -- тип числа (int или float)
        nbr_text        -- надпись, выводимая в запросе на ввод числа для пользователя
        nbr_cond        -- условие, налагаемое на число

        nbr_type. Если парамент принимает значение 'int', то получаем целое число.
        Любое другое значение выведет число с плавающей точкой

        nbr_cond. Передает уловие отбора чисел при помощи функции lambda.
        Если условие не передается, то передаем функцию следующего вида (lambda a: True)

        Пример вызова функции:
        1.
        text = '> Введите действительное положительное число x: '
        print(input_nbr('int',text,lambda a: True)      - ввод целого числа, условий нет

        2.
        text = '> Введите действительное положительное число x: '
        print(input_nbr('int', text, lambda a: a > 0))  - ввод целого числа, число больше нуля

        Много времени потратил, но уж слишком часто вызываются разные числа.
        Переделывать под разные условия каждый раз нудно
        Пока так. Дальше улучшу

    """
    value = input(f"{nbr_text}")  # пользователь вводит число
    while True:  # цикл закончится тогда, когда введенное значение будет числом с заданным условием
        # если введенное значение не число или не удовлетворяет условиям
        try:
            # пытаемся преобразовать переменную в целое число
            float(value)
            # если успешно, проверим, заданное условие
            if nbr_cond(            # условие передается функцией вида lambda a: a > 0
                    float(value)):
                break  # Если ввод правильный, выходим
        except ValueError:  # обработаем Перехват исключения
            # если введенное значение нельзя преобразовать в число
            # flag = False
            value = input(f"'Ошибка' {nbr_text}")
    # Если ввод верный, то возвращаем значение целым или с плавающей точкой.
    # В зависимости от запроса
    return int(float(value)) if nbr_type == 'int' else float(value)
# Определения используемых фукций конец //////////////////////////////////

# код программы начало ///////////////////////////////////////////////////
# содержит код основной программы из задания


def main():
    """
        содержит код основной программы из задания
    """

    # Программа принимает координаты точек прямой.
    print('Водим координаты первой точки:')
    text = '    > Введите координату X первой точки, целое действительное число: '
    x1_val = input_nbr('float', text, lambda a: a > 0)
    text = '    > Введите координату Y первой точки, целое действительное число: '
    y1_val = input_nbr('float', text, lambda a: a > 0)

    print('Водим координаты второй точки:')
    text = '    > Введите координату X второй точки, целое действительное число: '
    x2_val = input_nbr('float', text, lambda a: a > 0)
    text = '    > Введите координату Y второй точки, целое действительное число: '
    y2_val = input_nbr('float', text, lambda a: a > 0)

    # ищем угловой коэффициент
    k_val = (x1_val - x2_val) / (y1_val - y2_val)

    # ищем свободный член
    b_val = y1_val - k_val * x1_val

    print(
        f"\n Уравнение прямой, проходящей через эти точки: y = {k_val}x + {b_val}")


# ЭТО СОБСТВЕННО ВЫЗОВ КОДА ПРОГРАММЫ
main()                                  # ну, вперед!
# конец кода программы////////////////////////////////////////////////////
