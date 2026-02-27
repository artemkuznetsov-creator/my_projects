import random
import string

numbers = '0123456789'
n = int(input('Введите длину строки '))
data = string.ascii_letters + numbers
sentence = ''
for x in range(n):
    sentence += random.choice(data)
print(sentence)

stroka = ''
answer = []
for x in sentence:
    if x in numbers:
        stroka += x
    elif stroka == '':
        continue
    else:
        answer.append(stroka)
        stroka = ''
minimal = min(map(int, answer))
print(answer, minimal, len(str(minimal)))