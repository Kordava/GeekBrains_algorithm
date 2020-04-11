"""
2.	Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого это цифры числа.
Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

Подсказка:
Для решения задачи обязательно примените какую-нибудь коллекцию из модуля collections
Для лучшее освоения материала можете даже сделать несколько решений этого задания,
применив несколько коллекций из модуля collections
Также попробуйте решить задачу вообще без collections и применить только ваши знания по ООП
(в частности по перегрузке методов)
"""
from functools import reduce
# ВАРИАНТ 3. Через классы-------------------------------------------------


def very_simple(num_1, num_2):
    """
    самый простой вариант со встроенной функцией
    для проверки дальнейших расчетов
    """
    sum_simple = hex(int(num_1, 16) + int(num_2, 16))
    mult_simple = hex(int(num_1, 16) * int(num_2, 16))
    return sum_simple, mult_simple


class HexNum:
    """
    Работа с 16-ми числами
    """
    def __init__(self, hex_num):
        self._list_of_numbers = '0123456789ABCDEF'
        self.dec_num = self._from_hex_to_dec(hex_num)
        self.sum = 0
        self.mult = 0

    def __add__(self, other):
        self.sum = self.dec_num + other.dec_num
        self.sum = self._from_dec_to_hex(self.sum)

    def __mul__(self, other):
        self.mult = self.dec_num * other.dec_num
        self.mult = self._from_dec_to_hex(self.mult)

    def _from_hex_to_dec(self, hex_num):
        """
        Переводит число из 16-й системы в 10-ю
        """
        # для краткости используем reduce
        # Начинаем с высших разрядов, по достижении низших высшие умножатся на
        # разрядность 16
        dec_num = reduce(lambda x, y: x * 16 +
                         (self._list_of_numbers.find(y)), list(hex_num), 0)

        return dec_num

    def _from_dec_to_hex(self, dec_num):
        """
        Переводит число из 10-й системы в 16-ю
        """
        hex_num = []
        tmp_num = dec_num
        while True:
            tmp_num_chas = tmp_num // 16
            tmp_num_ost = tmp_num % 16
            hex_ost = list(self._list_of_numbers[tmp_num_ost])
            hex_num = hex_ost + hex_num

            if tmp_num_chas <= 16:
                hex_chas = list(self._list_of_numbers[tmp_num_chas])
                return hex_chas + hex_num
            tmp_num = tmp_num_chas

# Рабочая область


# сохраняем наши числа в переменых
NUM_1 = 'A2'
NUM_2 = 'C4F'

# создаем экземпляры класса для каждого числа
CL_NUM_1 = HexNum(NUM_1)
CL_NUM_2 = HexNum(NUM_2)

# суммируем и умножаем
RUN_CL = CL_NUM_1 + CL_NUM_2
RUN_CL = CL_NUM_1 * CL_NUM_2

# выводим результат
print(CL_NUM_1.sum)
print(CL_NUM_1.mult)

# Результаты выполнения
    # ('0xcf1', '0x7c9fe')
    # ['C', 'F', '1']
    # ['7', 'C', '9', 'F', 'E']
# Совпадает
