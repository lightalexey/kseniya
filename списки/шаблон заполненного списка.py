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
