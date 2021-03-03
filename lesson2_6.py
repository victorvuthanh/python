# 6. * Реализовать структуру данных «Товары». Она должна представлять собой список
# кортежей. Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть
# два элемента — номер товара и словарь с параметрами (характеристиками товара: название,
# цена, количество, единица измерения). Структуру нужно сформировать программно,
# т.е. запрашивать все данные у пользователя.
#
# Пример готовой структуры:
#
# [
#
# (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
# (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
# (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
# ]
#
# Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ —
# характеристика товара, например название, а значение — список значений-характеристик,
# например список названий товаров.
#
# Пример:
#
# {
#
# “название”: [“компьютер”, “принтер”, “сканер”],
# “цена”: [20000, 6000, 2000],
# “количество”: [5, 2, 7],
# “ед”: [“шт.”]
# }


order = 4

products = [(1, {'название': 'Ремень', 'цена': 40, "количество": 90, 'единица': 'шт.'}),
            (2, {'название': 'Носки', 'цена': 5, "количество": 190, 'единица': 'шт.'}),
            (3, {'название': 'Шарф', 'цена': 10, "количество": 45, 'единица': 'шт.'})]

print("\n".join("{}\t{}".format(k, v) for k, v in products))
while True:
    products.append((
        order,
        {
            'название': input('Введите название товара: '),
            'цена': input('Введите стоимость товара: '),
            'количество': input('Введите количество: '),
            'единица': input('Введите единицы измерения: ')
        }
    ))
    order += 1

    print("\n".join("{}\t{}".format(key, v) for key, v in products))

    q = input('Формирование списка завершено? (y/N)) ')
    if q.lower() == 'y' or q.lower() == 'н':
        break

analitics = {
    'название': [],
    'цена': [],
    'количество': [],
    'единица': set()
}

for el, item in products:
    analitics['название'].append(item['название'])
    analitics['цена'].append(item['цена'])
    analitics['количество'].append(item['количество'])
    analitics['единица'].add(item['единица'])

print("\n Аналитика о товарах\n")
for key, value in analitics.items():
    print(f'{key[:25]:<10}: {value}')


print('\nКонец программы')
