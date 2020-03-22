"""
Задание_1. В диапазоне натуральных чисел от 2 до 99 определить,
сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

Подсказка: используйте вложенный цикл

Пример:
В диапазоне 2-99: 49 чисел кратны 2
В диапазоне 2-99: 33 чисел кратны 3
В диапазоне 2-99: 24 чисел кратны 4
В диапазоне 2-99: 19 чисел кратны 5
В диапазоне 2-99: 16 чисел кратны 6
В диапазоне 2-99: 14 чисел кратны 7
В диапазоне 2-99: 12 чисел кратны 8
В диапазоне 2-99: 11 чисел кратны 9
"""
MY_LIST = [0] * 8
# проходим числа от 2 до 9 (J)
for j in range(2, 10):
    # Пробегаем последовательность 2-99 начиная с J с шагом J.
    # Тем самым идем по числам заведомо кратным J
    for i in range(j, 100, j):
        # на каждом щаге увеличиваем значение
        # соответствующего элемента списка на 1
        MY_LIST[j - 2] += 1
    # выводим на экран результат для числа J
    print(f"В диапазоне 2-99: {MY_LIST[j-2]:2d} чисел кратны {j}")