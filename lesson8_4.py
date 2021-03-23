'''
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
уникальные для каждого типа оргтехники.
'''


class Storage:
    def __init__(self):
        self._dict = {}

    def add_to(self, equipment):
        self._dict.setdefault(equipment.name, []).append(equipment)

    def extract(self, name):
        if self._dict[name]:
            self._dict.setdefault(name).pop(0)


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
        return 'Печатает'


class Scaner(Equipment):
    def __init__(self, name, make, year):
        super().__init__(name, make, year)

    def action(self):
        return 'Сканирует'


class Xerox(Equipment):
    def __init__(self, name, make, year):
        super().__init__(name, make, year)

    def action(self):
        return 'Копирует'


storage = Storage()
# создаем объект и добавляем
scaner = Scaner('hp', '321', 90)
storage.add_to(scaner)
printer = Printer(123, 'Samsung', '344', 20 )
storage.add_to(printer)
scaner = Scaner('hp', '311', 97)
storage.add_to(scaner)
xerox = Xerox('Xerox', '444', 21)
storage.add_to(xerox)
scaner = Scaner('hp', '330', 99)

storage.add_to(scaner)
print(storage._dict)

storage.extract('hp')
print(storage._dict)

xerox.action()
