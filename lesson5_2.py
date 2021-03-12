# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет
# количества строк, количества слов в каждой строке.

with open('lesson5_2.txt', 'r') as f:
    print(f.read())
    f.seek(0)
    lines = f.readlines()

    print(f'В файле "{f.name}" имеются {len(lines)} строк:')
    for index, value in enumerate(lines):
        number_of_words = len(value.split())
        print('{}-я строка имеет {} слов.'.format(index + 1, number_of_words))
print('\nКонец программы.')
