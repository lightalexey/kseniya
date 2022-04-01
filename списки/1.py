# from random import randrange
a = []
print('Исходный список:')
print(a)
n = int(input('Введи количество элементов:'))
for i in range(n):
    number = int(input('Введи число:'))
    a.append(number)
# print(*a)
for i in range(n):
    print(a[i], end=' ')