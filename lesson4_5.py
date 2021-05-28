# Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти четные числа от 100 до 1000 (включая границы). Необходимо получить результат
# вычисления произведения всех элементов списка. Подсказка: использовать функцию reduce().
from functools import reduce
from print_table import print_table

def my_func(x, y):
    return x * y
my_list = [el for el in range(100, 1001) if el % 2 == 0]

print(f'Список четных значений от 100 до 1000:')
print_table(my_list, 90, 4)

result = str(reduce(my_func, my_list))
print(f'Результат перемножения:')
print_table(result, 302, 1)

print('\nКонец программы')
