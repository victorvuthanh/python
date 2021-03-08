# Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти четные числа от 100 до 1000 (включая границы). Необходимо получить результат
# вычисления произведения всех элементов списка. Подсказка: использовать функцию reduce().

from functools import reduce

def my_func(x, y):
    return x * y
my_list = [el for el in range(100, 1001) if el % 2 == 0]

print(f'Список четных значений от 100 до 1000:')
from print_table import print_table
print_table(my_list, 50, 4)

print(f'Результат перемножения: {reduce(my_func, my_list)}')

print('\nКонец программы')
