# Реализовать два небольших скрипта:
#  а) бесконечный итератор, генерирующий целые числа, начиная с указанного,
#  б) бесконечный итератор, повторяющий элементы некоторого списка, определенного заранее.
#  Подсказка: использовать функцию count() и cycle()  модуля itertools.

from itertools import cycle, count

a = int(input('Введите стартовое число '))
for el in count(a):
    if el < a + 10:
        print(el)
    else:
        break
a = 0
my_list = [('q', 'w', 'e'), 'ABC', 123, None]
for el in cycle(my_list):
    if a < 10:
        print(el)
        a += 1
    else:
        break

print('\nКонец программы')