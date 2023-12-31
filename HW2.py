'''
Требуется найти в массиве list_1 
самый близкий по величине элемент к заданному числу k и вывести его.

Пример:
list_1 = [1, 2, 3, 4, 5]
k = 6
# 5
'''

list_1 = [1, 12, 6, 7, 8, 15]
k = 11
if k in list_1:
    print(k)
elif max(list_1) > k:
    while k not in list_1:
        k += 1
        for el in list_1:
            if k == el:
                print(k)
                break
else:
    while k not in list_1:
        k -= 1
        for el in list_1:
            if k == el:
                print(k)
                break

# правильный вариант

list_1 = [1, 12, 6, 7, 8, 15]
k = 9
m = abs(k - list_1[0])  # модуль числа
number = list_1[0]
for i in range(1, len(list_1)):
    if m > abs(list_1[i] - k):
        m = abs(list_1[i] - k)
        number = list_1[i]
print(number)