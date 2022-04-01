from random import randrange
a = []
print('Исходный список:')
n = 10
for i in range(n):
    a.append(randrange(101) - 50)
    print(a[i], end=' ')
# print(*a)
print()
# код начинается отсюда...
summa = 0
pro = 1
k = 0
kpol = 0
summapol = 0
for i in range(n):
    summa += a[i]
    if a[i] != 0:
      pro *= a[i]
    if a[i] % 2 == 0:
        k += 1
    if a[i] > 0:
        summapol += a[i]
        kpol += 1

print('Сумма элементов списка равна', summa)
print('Сумма элементов списка равна', sum(a))
print('произведение ненулевых элементов равно', pro)
print('реднее арифм =', summa / n)
print(k)
print('сумма положительных =', summapol)
print(kpol)
print(a[0], a[n - 1])
print(a[-1])