sentence = str(input('Введите предложение: '))
c = 0
for x in sentence:
    if x == 'с':
        sentence = sentence.replace('с','', 1)
        c +=1

print('Ваша строка: ', sentence , 'Количесвто "с": ', c)
