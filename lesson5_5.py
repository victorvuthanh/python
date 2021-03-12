# 5. Создать (программно) текстовый файл, записать в него программно набор чисел,
# разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

FLOATING_STR = "4 1.5 2 2.5 0"
summ = 0.0

with open('lesson5_5.txt', 'w') as f:
    f.write(FLOATING_STR)

with open('lesson5_5.txt') as f:
    data = f.read()

for item in data.split():
    summ += float(item)

print(f'Сумма чисел в файле {f.name} = {summ}')
print('\nКонец программы.')
