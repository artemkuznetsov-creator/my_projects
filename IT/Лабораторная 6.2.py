sentence = str(input())
numbers = '0123456789'
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
if stroka != '':
    answer.append(stroka)
minimal = min(map(int, answer))
print(answer)
print(len(str(minimal)))






