a = (13, 5, 43, 49, 67, 32, 12, 98, 6, 10, 34, 20, 55, 68, 14, 60, 14)
b = (53, 21, 4, 23, 76, 3, 43, 12, 54, 342, 21)

s_a = sum(a)
s_b = sum(b)



if s_a > s_b:
    print('Сумма кортежа - a')
else:
    print('Cумма кортежа - b')

print('min a', min(a), 'Номер - ', a.index(min(a)) + 1)
print('min b', min(b), 'Номер - ', b.index(min(b)) + 1)

print(s_a)
print(s_b)
