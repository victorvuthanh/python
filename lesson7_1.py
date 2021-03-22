'''
1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.

Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц вы найдете в методичке.

Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.

Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов
класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.

Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки
первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.
'''

import random

class Matrix:

    def __init__(self, m, n, init=True):
        if init:
            self.rows = [[0] * n for x in range(m)]
        else:
            self.rows = []
        self.m = m
        self.n = n

    def __getitem__(self, idx):
        return self.rows[idx]

    def __setitem__(self, idx, item):
        self.rows[idx] = item

    def __str__(self):
        s = '\n'.join([' '.join([str(item) for item in row]) for row in self.rows])
        return s + '\n'

    def __add__(self, mat):

        ret = Matrix(self.m, self.n)

        for x in range(self.m):
            row = [sum(item) for item in zip(self.rows[x], mat[x])]
            ret[x] = row

        return ret

    @classmethod
    def makeRandom(cls, m, n, low=0, high=10):

        obj = Matrix(m, n, init=False)
        for x in range(m):
            obj.rows.append([random.randrange(low, high) for i in range(obj.n)])

        return obj


m = Matrix.makeRandom(3, 3)
print(f'Первая матрица: \n{m}')

n = Matrix.makeRandom(3, 3)
print(f'Вторая матрица: \n{n}')

print(f'Сумма матрицы: \n{m + n}')

print('Конец программы')