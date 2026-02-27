from random import choice
letters = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
n = int(input('Введите длину строки: '))
sentence = ''
for i in range(n):
    sentence += choice(letters)
c = 0
print(sentence)
for x in sentence:
    if x == 'с':
        sentence = sentence.replace('с','', 1)
        c +=1

print('Ваша строка: ', sentence , 'Количесвто "с": ', c)

