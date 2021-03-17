'''
3. Реализовать базовый класс Worker (работник), в котором определить
атрибуты: name, surname, position (должность), income (доход). Последний атрибут должен быть
защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
и дохода с учетом премии (get_total_income). Проверить работу примера на реальных данных
(создать экземпляры класса Position, передать данные, проверить значения атрибутов,
вызвать методы экземпляров).
'''


class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):

    def get_full_name(self):
        return ' '.join([self.surname, self.name])

    def get_total_income(self):
        return sum(self._income.values())


if __name__ == '__main__':
    position_data = [
        {
            'name': 'Владимир',
            'surname': 'Медведев',
            'position': 'Водитель',
            'wage': 40000,
            'bonus': 20000
        },
        {
            'name': 'Сергей',
            'surname': 'Иванов',
            'position': 'Директор',
            'wage': 90000,
            'bonus': 60000
        },
        {
            'name': 'Ирина',
            'surname': 'Иванова',
            'position': 'Менеджер',
            'wage': 60000,
            'bonus': 30000
        },
    ]

    for item in position_data:
        position = Position(**item)
        print('Исходные данные: ', item)
        print('Фамилия Имя: ', position.get_full_name())
        print(f'Доход: {position.get_total_income()} \n')

print('\nКонец программы')
