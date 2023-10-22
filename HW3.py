'''В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.

В случае с английским алфавитом очки распределяются так:
A, E, I, O, U, L, N, S, T, R – 1 очко;
D, G – 2 очка;
B, C, M, P – 3 очка;
F, H, V, W, Y – 4 очка;
K – 5 очков;
J, X – 8 очков;
Q, Z – 10 очков.

А русские буквы оцениваются так:
А, В, Е, И, Н, О, Р, С, Т – 1 очко;
Д, К, Л, М, П, У – 2 очка;
Б, Г, Ё, Ь, Я – 3 очка;
Й, Ы – 4 очка;
Ж, З, Х, Ц, Ч – 5 очков;
Ш, Э, Ю – 8 очков;
Ф, Щ, Ъ – 10 очков.
Напишите программу, 
которая вычисляет стоимость введенного пользователем слова k и выводит его. 
Будем считать, что на вход подается только одно слово, 
которое содержит либо только английские, либо только русские буквы.

Пример:
k = 'ноутбук'
# 12
'''

k = 'ноутбук'
new_k = k.upper()
sum = 0
for letter in new_k:
    if letter == 'A' or letter == 'E' or letter == 'I' or letter == 'O' or letter == 'U' or letter == 'L' or letter == 'N' or letter == 'S' or letter == 'T' or letter == 'R' or letter == 'А' or letter == 'В' or letter == 'Е' or letter == 'И' or letter == 'Н' or letter == 'О' or letter == 'Р' or letter == 'С' or letter == 'Т':
        sum += 1
    elif letter == 'D' or letter == 'G' or letter == 'Д' or letter == 'К' or letter == 'Л' or letter == 'М' or letter == 'П' or letter == 'У':
        sum += 2
    elif letter == 'B' or letter == 'C' or letter == 'M' or letter == 'P' or letter == 'Б' or letter == 'Г' or letter == 'Ё' or letter == 'Ь' or letter == 'Я':
        sum += 3
    elif letter == 'F' or letter == 'H' or letter == 'V' or letter == 'W' or letter == 'Y' or letter == 'Й' or letter == 'Ы':
        sum += 4
    elif letter == 'K' or letter == 'Ж' or letter == 'З' or letter == 'Х' or letter == 'Ц' or letter == 'Ч':
        sum += 5
    elif letter == 'J' or letter == 'X' or letter == 'Ш' or letter == 'Э' or letter == 'Ю':
        sum += 8
    elif letter == 'Q' or letter == 'Z' or letter == 'Ф' or letter == 'Щ' or letter == 'Ъ':
        sum += 10
print(sum)

# верный вариант
k = 'ноутбук'
points_en = {1: 'AEIOULNSTR', 2: 'DG', 3: 'BCMP', 4: 'FHVWY', 5: 'K', 8: 'JX', 10: 'QZ'}
points_ru = {1: 'АВЕИНОРСТ', 2: 'ДКЛМПУ', 3: 'БГЁЬЯ', 4: 'ЙЫ', 5: 'ЖЗХЦЧ', 8: 'ШЭЮ', 10: 'ФЩЪ'}
word = k.upper()  # переводим все буквы в верхний регистр
count = 0
for i in word:
    if i in 'QWERTYUIOPASDFGHJKLZXCVBNM':
        for j in points_en:
            if i in points_en[j]:
                count = count + j
    else:
        for j in points_en:
            if i in points_ru[j]:
                count = count + j
print(count)
