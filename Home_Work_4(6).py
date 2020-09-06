from sys import argv
from itertools import count, cycle

script_name, x_1, x_2, y_1, y_2 = argv

print('Введите первый элемент: ', x_1)
print('Введите последний элемент: ', x_2)
list_1 = []
for i in count(int(x_1)):
    if i > int(x_2):
        break
    else:
        list_1.append(i)

print('Полученная последовательность: ', list_1)


print('Введите последовательность: ', y_1)
print('Введите количество итераций: ', y_2)

list_2 = []
n = 0
for i in cycle(y_1):
    if n > int(y_2):
        break
    else:
        list_2.append(i)
        n += 1

print('Полученная последовательность: ', list_2)
