from random import randrange
a = []
print('Исходный список:')
n = 10
for i in range(n):
    a.append(randrange(-50, 50))  # [-50;50]
    print(a[i], end=' ')
# print(*a)
print()
# код начинается отсюда...
maximum = a[0]
minimum = a[0]
secondmaximum = a[0]
secondminimum = a[0]
inmax = 0
inmin = 0
secondinmax = 0
secondinmin = 0
for i in range(n):
    if a[i] > maximum:
        maximum = a[i]
        inmax = i
    if a[i] < minimum:
        minimum = a[i]
        inmin = i
for i in range(n):
    if a[i] > secondmaximum and a[i] != maximum:
                secondmaximum = a[i]
                secondinmax = i
    if a[i] < secondminimum and a[i] != minimum:
                secondminimum = a[i]
                secondinmin = i


print('max:', maximum,inmax)
print('min:', minimum, inmin)
print('второе максимальное =', secondmaximum, secondinmax)
print('второе минимальное =', secondminimum, secondinmin)