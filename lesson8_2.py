'''
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем.
При вводе пользователем нуля в качестве делителя программа должна корректно
обработать эту ситуацию и не завершиться с ошибкой.
'''

class DivisionByZero:
    def __init__(self, divider, denominator):
        self.divider = divider
        self.denominator = denominator

    @staticmethod
    def divide_by_null(divider, denominator):
        try:
            return print(f'{divider} / {denominator} = {divider / denominator}')
        except:
            return print(f'{divider} / {denominator}  - Деление на ноль недопустимо')

DivisionByZero.divide_by_null(10, 0)
DivisionByZero.divide_by_null(10, 0.1)
DivisionByZero.divide_by_null(100, 0)