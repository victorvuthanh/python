'''
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
уникальные для каждого типа оргтехники.
'''


class Storage:
    def __init__(self):
        self._dict = {}

class Equipment:
    def __init__(self, name, make, year):
        self.name = name
        self.make = make
        self.year = year

    def __repr__(self):
        return f'{self.name}-{self.make}-{self.year}'


class Printer(Equipment):
    def __init__(self, series, name, make, year):
        super().__init__(name, make, year)
        self.series = series

    def action(self):
        return print(f'{self.name} Печатает')


class Scaner(Equipment):
    def __init__(self, name, make, year):
        super().__init__(name, make, year)

    def action(self):
        return print(f'{self.name} сканирует')


class Xerox(Equipment):
    def __init__(self, name, make, year):
        super().__init__(name, make, year)

    def action(self):
        return print(f'{self.name} копирует')

scaner = Scaner('hp', '321', 90)
printer = Printer(123, 'Samsung', '344', 20 )
scaner1 = Scaner('hp', '311', 97)
xerox = Xerox('Xerox', '444', 21)
scaner2 = Scaner('hp', '330', 99)

printer.action()
scaner.action()
xerox.action()