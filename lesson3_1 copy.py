# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def div(*args):
    try:
        arg1 = int(input("Ввод делимое: "))
        arg2 = int(input("Ввод делитель "))
        res = arg1 / arg2
    except ValueError:
        return 'Вводимые данные должны быть числом'
    except ZeroDivisionError:
        return "Попытка деления на ноль"
    return res

print('Результат: ', div(), '\n\nКонец программы')
