'''
4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
speed, color, name, is_police (булево). А также методы: go, stop, turn(direction),
которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, Sportown_car, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости
свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам,
выведите результат. Выполните вызов методов и также покажите результат.
'''


class Car:
    __speed = 0
    __direction = None

    def __init__(self, speed, color, name, is_police):
        self.__speed = speed
        self.speed = 0
        self.color = color
        self.name = name
        self.is_police = is_police

    def stop(self):
        self.speed = 0

    def turn(self, direction):
        print(f'{self.name} поворачивает налево') if direction == 'left' \
            else print(f'{self.name} поворачивает направо')

    def show_speed(self):
        print(f'Текущая скорость автомобиля {self.name}: {self.speed}км/ч')

    def go(self):
        self.speed = self.__speed


class TownCar(Car):
    MAX_SPEED = 60

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)

    def show_speed(self):
        print(f'Текущая скорость автомобиля {self.name}: {self.speed}км/ч')
        if self.speed > self.MAX_SPEED:
            print(f'>>Превышение скорости автомобилем {self.name} на {self.speed - self.MAX_SPEED}!<<')


class Sportcar(Car):

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)


class WorkCar(Car):
    MAX_SPEED = 40

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)

    def show_speed(self):
        print(f'Текущая скорость автомобиля {self.name}: {self.speed}км/ч')
        if self.speed > self.MAX_SPEED:
            print(f'>>Превышение скорости автомобилем {self.name} на {self.speed - self.MAX_SPEED}!<<')


class PoliceCar(Car):

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, True)


if __name__ == '__main__':
    police_car = PoliceCar(120, 'Синий', 'FORD')
    work_car1 = WorkCar(30, 'Белый', 'BMW G3')
    work_car2 = WorkCar(90, 'Серый', 'BMW G4')
    sport_car = Sportcar(200, 'Красный', 'Audi')
    town_car1 = TownCar(80, 'Черный', 'Lada 3000')
    town_car2 = TownCar(50, 'Синий', 'Lada 5000')

    police_car.show_speed()
    police_car.go()
    police_car.show_speed()
    police_car.stop()
    police_car.show_speed()
    print(f'Цвет автомобиля {police_car.name} : {police_car.color}')
    if police_car.is_police:
        print(f'{police_car.name} является полицейским автомобилем')
    else:
        print(f'{police_car.name} не является полицейским автомобилем')
    work_car1.go()
    work_car2.go()
    sport_car.go()
    town_car1.go()
    town_car2.go()
    work_car1.show_speed()
    work_car2.show_speed()
    sport_car.show_speed()
    town_car1.show_speed()
    town_car2.show_speed()
    sport_car.turn('left')
    if sport_car.is_police:
        print(f'{sport_car.name} является полицейским автомобилем')
    else:
        print(f'{sport_car.name} не является полицейским автомобилем')

    sport_car.turn('right')

print('\nКонец программы')