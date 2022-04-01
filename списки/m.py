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
inmax = 0
inmin = 0
for i in range(n):
    if a[i] > maximum:
        maximum = a[i]
        inmax = i
    if a[i] < minimum:
        minimum = a[i]
        inmin = i


print('max:', maximum,inmax)
print(minimum, inmin)
print()