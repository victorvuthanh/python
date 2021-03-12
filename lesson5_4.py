# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться
# в новый текстовый файл.

dictionary = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
new_list = []
with open('lesson5_4.txt', 'r') as file:
    for line in file:
        i = line.split(' ', 1)
        new_list.append(dictionary[i[0]] + ' ' + i[1])

with open('lesson5_4_new.txt', 'w') as file:
    file.writelines(new_list)

print(f'Смотрите файл {file.name}!\nКонец программы.')
